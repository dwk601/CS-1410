#Select 10 countries at random from flags.txt 
# and download each flag file in a file name Country_Name.jpg,
# where Country_Name is the country name contained in the flags.txt file. 
# The USA flag would be stored in the file United_States.jpg, for example.

#To download a flag, call curl in a subprocess, 
# using the subprocess module, receiving its output back into your program. 
# Then open a new file with the appropriate Country_Name.jpg name, 
# for binary output, and save the downloaded content into that file.

#Accumulate the length in bytes of each file 
# and report the total number of bytes downloaded to the console. 

def random_country(n): #n is the number of countries to be selected
    import random
    countries = []
    with open('flags.txt') as f:
        for line in f:
            countries.append(line.strip())
    return random.sample(countries, n)

def download_flag(country):
    import subprocess
    url = 'https://www.cia.gov/library/publications/resources/the-world-factbook/graphics/flags/large/' + country.lower().replace(' ', '-') + '-lgflag.gif'
    subprocess.run(['curl', '-o', country + '.jpg', url])
            
def main():
    countries = random_country(10)
    total_bytes = 0
    for country in countries:
        download_flag(country)
        with open(country + '.jpg', 'rb') as f:
            total_bytes += len(f.read())
    print('Total bytes downloaded: ' + str(total_bytes))

if __name__ == '__main__':
    main()
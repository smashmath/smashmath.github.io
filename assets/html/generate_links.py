# crawl this directory and generate a list of links to all the files in it
# ex. introduction.html: https://smashmath.github.io/assets/html/introduction.html
# output: assets/html/links.txt
# usage: python generate_links.py

import os

def generate_links():
    # get the current directory
    current_dir = os.path.dirname(os.path.realpath(__file__))
    # get the parent directory
    parent_dir = os.path.dirname(current_dir)
    # get the list of files in the current directory
    files = os.listdir(current_dir)
    # open the output file
    output = open(parent_dir + '/links.txt', 'w')
    # iterate through the files
    for file in files:
        if not file.endswith('.html'):
            continue
        # get the path to the file
        path = current_dir + '/' + file
        # get the link to the file
        link = 'https://smashmath.github.io/' + path.split(parent_dir)[1]
        # write the link to the output file
        output.write(file + ':\n\t' + link + '\n')
    # close the output file
    output.close()
    
generate_links()
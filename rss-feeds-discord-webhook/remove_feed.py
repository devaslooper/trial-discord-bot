from json import load, dump
key = input("Title: ")
with open("feed_links.json","r") as input_file:
    existing_links = load(input_file)
del existing_links[key]
with open("datafile.json","r") as input_data_file:
    existing_data = load(input_data_file)
del existing_data[key]
with open("datafile.json","w") as output_data_file:
    dump(existing_data,output_data_file,indent=4)
with open("feed_links.json","w") as output_file:
    dump(existing_links,output_file,indent=4)
# funkcja wczytujaca dane; na wejsciu dostaje nazwe pliku; na wyjsciu zwraca liste wczytanych elementow
def read_data(datafile):
    extracted_data = [i.strip().split() for i in open(datafile)]
    flat_list = [int(item) for sublist in extracted_data for item in sublist]
    return flat_list


# przykladowe dane do funkcji merge_islands():
# wyspy przed scaleniem:
# [1,5,4,7,6,8]
# wyspy po scaleniu:
# [1,8]

# przykladowe dane do funkcji create_map() dla n=25, d=2, oraz scalonych wysp: [0, 0, 2, 5, 10, 11, 19, 21]
# ['|','-','|','|','|','|','-','-','-','-','|','|','-','-','_','_','_','-','-','|','|','|','-','-','_']

from cassis import *
import csv
from nltk.tokenize import word_tokenize

sentence_id = 0
number = 0

max_length = 0
min_length = 10000
sum_length = 0
count = 0

annotator_1 = [['Annotator_1','Annotated_part_1','Final_Dataset_tsv'],['Annotator_1','Annotated_part_2','ratemy_professor_data_from_sorted_list_shuffle_1']]
annotator_2=[['Annotator_3','Annotated_part_6','Final_Dataset_tsv']]
annotator_3 = [['Annotator_2','Annotated_part_3','Final_Dataset_tsv'],['Annotator_2','Annotated_part_4','ratemy_professor_data_from_sorted_list_shuffle_1'],['Annotator_2','Annotated_part_5','additional_100_of_rate_my_proffesor']]
annotators = [annotator_1,annotator_2,annotator_3]
path_for_folder = "/content/drive/Shareddrives/FYP/Annotated Data/"    ## change this path to Annotated Data folder

with open(path_for_folder+'Annotator_3/Annotated_part_6/TypeSystem.xml', 'rb') as f: # get all annotated tagsets
  typesystem_tmp = load_typesystem(f)
for annotator in annotators:
  for path_for_data in annotator:  


    with open('/content/drive/Shareddrives/FYP/Annotated Data/'+path_for_data[0]+'/'+path_for_data[1]+'/'+path_for_data[2]+'.xmi', 'rb') as f:  #read all annotated dataset one by one
      doc_tmp = load_cas_from_xmi(f, typesystem=typesystem_tmp)

    data = doc_tmp.sofa_string
    for (_, sentence) in enumerate(doc_tmp.select('webanno.custom.'+"Document_levelopinion")):  #_to get sentences seperately
      if sentence.Document_levelopinion != None:
        count +=1
        length = len(word_tokenize(sentence.get_covered_text()))
        sum_length += (length)
        if length > max_length:
          max_length = length
        if length < min_length:
          min_length = length
print("max = ",max_length)
print("min = ",min_length)
print("sum = ",sum_length/count)
# # import math
# # import re
# # from collections import Counter
# #
# # WORD = re.compile(r'\w+')
# #
# #
# # def get_cosine(vec1, vec2):
# #     # print vec1, vec2
# #     intersection = set(vec1.keys()) & set(vec2.keys())
# #     numerator = sum([vec1[x] * vec2[x] for x in intersection])
# #
# #     sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
# #     sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
# #     denominator = math.sqrt(sum1) * math.sqrt(sum2)
# #
# #     if not denominator:
# #         return 0.0
# #     else:
# #         return float(numerator) / denominator
# #
# #
# # def text_to_vector(text):
# #     return Counter(WORD.findall(text))
# #
# #
# # def get_similarity(a, b):
# #     a = text_to_vector(a.strip().lower())
# #     b = text_to_vector(b.strip().lower())
# #
# #     return get_cosine(a, b)
# #
# #
# # print(get_similarity('Lusine and Adrine', 'Lusine and Adine'))
# import re, math
# from collections import Counter
# from nltk.corpus import stopwords
# from nltk.stem.porter import *
# from nltk.corpus import wordnet as wn
#
# stop = stopwords.words('english')
#
# WORD = re.compile(r'\w+')
# stemmer = PorterStemmer()
#
#
# def get_cosine(vec1, vec2):
#     # print vec1, vec2
#     intersection = set(vec1.keys()) & set(vec2.keys())
#     numerator = sum([vec1[x] * vec2[x] for x in intersection])
#
#     sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
#     sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
#     denominator = math.sqrt(sum1) * math.sqrt(sum2)
#
#     if not denominator:
#         return 0.0
#     else:
#         return float(numerator) / denominator
#
#
# def text_to_vector(text):
#     words = WORD.findall(text)
#     a = []
#     for i in words:
#         for ss in wn.synsets(i):
#             a.extend(ss.lemma_names())
#     for i in words:
#         if i not in a:
#             a.append(i)
#     a = set(a)
#     w = [stemmer.stem(i) for i in a if i not in stop]
#     return Counter(w)
#
#
# def get_similarity(a, b):
#     a = text_to_vector(a.strip().lower())
#     b = text_to_vector(b.strip().lower())
#
#     return get_cosine(a, b)
#
#
# def get_char_wise_similarity(a, b):
#     a = text_to_vector(a.strip().lower())
#     b = text_to_vector(b.strip().lower())
#     s = []
#
#     for i in a:
#         for j in b:
#             s.append(get_similarity(str(i), str(j)))
#     try:
#         return sum(s) / float(len(s))
#     except:  # len(s) == 0
#         return 0
#
#
# print(get_similarity('I am a good boy', 'I am a very disciplined guy'))
# # Returns 0.5491201525567068
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

print(fuzz.ratio("Catherine M Gitau","Catherine Gitau"))
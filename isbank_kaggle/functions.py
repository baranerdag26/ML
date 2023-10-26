import numpy as np

def jaccard_similarity_score(true_values, predicted_values):
    # Her bir deneme için Jaccard benzerlik skorlarını hesaplamak için boş bir liste oluşturun
    jaccard_scores = []

    # Her deneme için işlemleri yapın
    for true, pred in zip(true_values, predicted_values):
        intersection = np.sum(np.minimum(true, pred))
        union = np.sum(np.maximum(true, pred))
        jaccard = intersection / union
        jaccard_scores.append(jaccard)

    # Deneme skorlarının ortalamasını hesaplayın
    average_jaccard_score = np.mean(jaccard_scores)

    return average_jaccard_score

def target_to_binary(target):
    # target sütununu dönüştürmek için bir işlev tanımlayın
    binary_target = ""
    for i in range(1, 10):
        if f'menu{i}' in target:
            binary_target += '1'
        else:
            binary_target += '0'
    return binary_target

def get_top3_menus(predictions):
  # Her satır için en yüksek 3 olasılığa sahip menü indekslerini bul
  top3_indices = predictions.argsort()[-3:][::-1]  
  
  # Bu indekslere göre binary vektör oluştur
  top3_binary = [0] * 9
  for idx in top3_indices:
    top3_binary[idx] = 1

  return top3_binary

from itertools import combinations

def generate_binary_numbers_with_three_ones():
    binary_numbers = []
    for combination in combinations(range(9), 3):
        binary_number = ['0'] * 9
        for index in combination:
            binary_number[index] = '1'
        binary_numbers.append(''.join(binary_number))
    return binary_numbers

def map_binary_to_integer(binary_str):
    binary_numbers = generate_binary_numbers_with_three_ones()
    if binary_str in binary_numbers:
        return binary_numbers.index(binary_str)
    else:
        return None

def map_integer_to_binary(integer):
    #map_binary_to_integer fonksiyonunun tersi. ancak numpy.ndarray tipindeki bir dizi için çalışır.
    binary_numbers = generate_binary_numbers_with_three_ones()
    if integer < len(binary_numbers):
        return binary_numbers[integer]
    else:
        return None

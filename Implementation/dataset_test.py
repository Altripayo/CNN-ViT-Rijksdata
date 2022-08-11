from sklearn.utils import shuffle
from library.dataset.date_dataset import DateDataset
from library.dataset.format_dataset import FormatDataset
from torch.utils.data import DataLoader

dataset = FormatDataset("data/rijksdata/")
loader = DataLoader(dataset, batch_size = 1, shuffle=True)

dict = {
            "aardewerk" : 0,
            "brons" : 1,
            "chine collé" : 2,
            "dekverf" : 3,
            "doek" : 4,
            "eikenhout" : 5,
            "email" : 6,
            "faience" : 7,
            "fluweel" : 8,
            "fotodrager" : 9,
            "geprepareerd papier" : 10,
            "glas" : 11,
            "glas-in-lood" : 12,
            "glazuur" : 13,
            "gouache (waterverf)" : 14,
            "goud" : 15,
            "goudkleurig bladmetaal" : 16,
            "grafiet" : 17,
            "grisailleverf" : 18,
            "hout" : 19,
            "ijzer" : 20,
            "inkt" : 21,
            "ivoor" : 22,
            "kant (materiaal)" : 23,
            "karton" : 24,
            "katoen" : 25,
            "kobalt" : 26,
            "koper" : 27,
            "kraakporselein" : 28,
            "krijt" : 29,
            "lak" : 30,
            "leer" : 31,
            "linnen" : 32,
            "lood" : 33,
            "marmer" : 34,
            "messing" : 35,
            "metaal" : 36,
            "notenhout" : 37,
            "olieverf" : 38,
            "paneel" : 39,
            "parelmoer" : 40,
            "perkament" : 41,
            "porselein" : 42,
            "potlood" : 43,
            "steengoed" : 44,
            "terracotta" : 45,
            "tin" : 46,
            "tinglazuur" : 47,
            "verf" : 48,
            "verguldsel" : 49,
            "waterverf" : 50,
            "wol" : 51,
            "zijde" : 52,
            "zilver" : 53,
            "zilverdraad" : 54
            }

count = 0
for (x, y) in loader:
    print("Format: " + str(y))
    count = count + 1
    if count > 10:
        break
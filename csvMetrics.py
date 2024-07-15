from datasets import load_dataset

class CodeMetrics:
    def __init__(self):
        self.unknown_source = 0
        self.codechef_source = 0
        self.codeforces_source = 0
        self.hackerearth_source = 0
        self.codeJam_source = 0
        self.atCoder_source = 0
        self.aizu_source = 0

        self.is_description_translated = 0

        self.unknown_language = 0
        self.python2_language = 0
        self.cpp_language = 0
        self.python3_language = 0
        self.java_language = 0

        self.entries = 0
    
    def increment_unknown_source(self):
        self.unknown_source += 1
    
    def increment_codechef_source(self):
        self.codechef_source += 1
    
    def increment_codeforces_source(self):
        self.codeforces_source += 1
    
    def increment_hackerearth_source(self):
        self.hackerearth_source += 1
    
    def increment_codeJam_source(self):
        self.codeJam_source += 1
    
    def increment_atCoder_source(self):
        self.atCoder_source += 1
    
    def increment_aizu_source(self):
        self.aizu_source += 1
    
    def increment_description_translation(self):
        self.is_description_translated += 1
    
    def increment_unknown_language(self):
        self.unknown_language += 1
    
    def increment_python2_language(self):
        self.python2_language += 1
    
    def increment_cpp_language(self):
        self.cpp_language += 1
    
    def increment_python3_language(self):
        self.python3_language += 1
    
    def increment_java_language(self):
        self.java_language += 1

    def print_metrics(self):
        print("Metrics:")
        print(f"Unknown Source: {self.unknown_source}")
        print(f"CodeChef Source: {self.codechef_source}")
        print(f"Codeforces Source: {self.codeforces_source}")
        print(f"Hackerearth Source: {self.hackerearth_source}")
        print(f"CodeJam Source: {self.codeJam_source}")
        print(f"ATCoder Source: {self.atCoder_source}")
        print(f"Aizu Source: {self.aizu_source}")
        print(f"Is Description Translated: {self.is_description_translated}")
        print(f"Unknown Language: {self.unknown_language}")
        print(f"Python2 Language: {self.python2_language}")
        print(f"C++ Language: {self.cpp_language}")
        print(f"Python3 Language: {self.python3_language}")
        print(f"Java Language: {self.java_language}")
        print(f"Total entries: {self.entries}")

code_metrics = CodeMetrics()


# Carrega o dataset deepmind/code_contests do Hugging Face
dataset = load_dataset('deepmind/code_contests')

# Acessa o conjunto de dados de treinamento
train_dataset = dataset['train']

total_lines = len(train_dataset)

code_metrics.entries = total_lines
print(total_lines)

for idx,line in enumerate(train_dataset):
    solutions = line['solutions']  # Acessa a coluna 'solutions' de cada exemplo
    languages = solutions['language']  # Extrai o vetor 'language'
    percent_done = (idx + 1) / total_lines * 100
    source = line['source']
    is_description_translated = line['is_description_translated']

    if is_description_translated == True:
        code_metrics.is_description_translated += 1

    match source:
        case 0:
            code_metrics.unknown_source += 1
        case 1:
            code_metrics.codechef_source += 1
        case 2:
            code_metrics.codeforces_source += 1
        case 3:
            code_metrics.hackerearth_source += 1
        case 4:
            code_metrics.codeJam_source += 1
        case 5:
            code_metrics.atCoder_source += 1
        case 6:
            code_metrics.aizu_source += 1

    for language in languages:
        match language:
            case 0:
                code_metrics.unknow_language += 1
            case 1:
                code_metrics.python2_language += 1
            case 2:
                code_metrics.cpp_language += 1
            case 3:
                code_metrics.python3_language += 1
            case 4:
                code_metrics.java_language += 1
    
    print(f"Progresso: {percent_done:.2f}%")

code_metrics.print_metrics()

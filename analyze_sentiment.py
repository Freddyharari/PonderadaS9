from transformers import pipeline

# Criar uma pipeline de análise de sentimentos
sentiment_analysis = pipeline("sentiment-analysis")

# Texto a ser analisado
text = "I am very happy with the service!"

# Analisar o sentimento do texto
result = sentiment_analysis(text)

# Imprimir o resultado
print(result)

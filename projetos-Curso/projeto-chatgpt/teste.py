import openai
#passar chave
openai.api_key = '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'
#define entrada
message = {'role':'user', 'content':'olá, você está funcionando?'}
messages = []
messages.append(message)
#chamando api
response = openai.ChatCompletion.create(model='gpt-3.5-turbo',messages=messages)
#imprimir response
print(response)
      #.choice[0].message.content)

      
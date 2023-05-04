from pygpt4all.models.gpt4all import GPT4All


def new_text_callback(text):
    print(text, end="")


model = GPT4All('./models/gpt4all-converted.bin')
# model.generate("Once upon a time, ", n_predict=55,
#                new_text_callback=new_text_callback)
for token in model.generate("Tell me 2+2 ?\n"):
    print(token, end='', flush=True)

# while True:
#     try:
#         prompt = input("You: ", flush=True)
#         if prompt == '':
#             continue
#         print(f"AI:", end='')
#         for token in model.generate(prompt):
#             print(f"{token}", end='', flush=True)
#         print()
#     except KeyboardInterrupt:
#         break

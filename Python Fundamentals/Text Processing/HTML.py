title = input()
content = input()
comments = []
while True:
    comment = input()
    if comment == 'end of comments':
        break
    comments.append(f"<div>\n\t {comment}\n</div>")

print(f"<h1>\n\t{title}\n</h1>")
print(f"<article>\n\t {content}\n</article>")
for i in comments:
    print(i)
adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

#1
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
#print(adwentures_of_tom_sawer)

#2
adwentures_of_tom_sawer =  adwentures_of_tom_sawer.replace("....", " ")
#print(adwentures_of_tom_sawer)

#3
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("  ", " ")
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer.split())
#print(adwentures_of_tom_sawer)

#4
adwentures_of_tom_sawer_with_h = adwentures_of_tom_sawer.count("h")
#print(adwentures_of_tom_sawer_with_h)

#5
count=0
for world in adwentures_of_tom_sawer.split():
    if world[0].isupper():
        count += 1
#print(count)

#6
position= adwentures_of_tom_sawer.find("Tom", adwentures_of_tom_sawer.find("Tom")+1)
#print(position)

#7
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(".")
#print(adwentures_of_tom_sawer_sentences)

#8
fourth_sentence= adwentures_of_tom_sawer_sentences[3].lower()
#print(fourth_sentence)

#9
#print("By the time" in adwentures_of_tom_sawer)
 
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.strip().startswith("By the time"):
        print(adwentures_of_tom_sawer_sentences.index(sentence))

#10
last_sentence = adwentures_of_tom_sawer_sentences[-2]
words_count = len(last_sentence.split())

print(words_count)
print(adwentures_of_tom_sawer_sentences)
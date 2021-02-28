import threading

tr_dict = dict()
mutex = threading.Lock()
prohibited = (',','.','?','!','-','+','\'','@')

def Count_trigrams(in_str):
	trgrms = dict()
	trgrm = ""
	for i in in_str:
		if i not in prohibited:
			trgrm += i
		else:
			trgrm = ""

		if len(trgrm) == 3:
			if trgrm in trgrms:
				trgrms[trgrm] += 1
			else:
				trgrms[trgrm] = 1
			trgrm = trgrm[1:]
	Add_to_global(trgrms)

def Add_to_global(trgrms):
	for i in trgrms:
		mutex.acquire()
		if i in tr_dict:
			tr_dict[i] += trgrms[i]
		else:
			tr_dict[i] = trgrms[i]
		mutex.release()

in_str = input("input your string here:\n")
strs = in_str.split()

threads = [
	threading.Thread(target = Count_trigrams, args = (s,))
	for s in strs
]
for t in threads:
	t.start()
for t in threads:
	t.join()

print(tr_dict)
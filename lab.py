def generate_trie(words):
	trie = {"frequency": 0, "children": {}}
	for word in words:
		current = trie
		for i in range(len(word)):
			letter = word[i]
			if letter not in current["children"]:
				current["children"][letter] = {"frequency": 0, "children": {}}
			current = current["children"][letter]
			if i == len(word)-1:
					current["frequency"] += 1
	return trie

def all_words(trie):
	words = {}
	traverse(trie, words, "")
	return words

def traverse(trie, words, prefix):
	if len(trie["children"]) == 0:
		return [""]

	else:
		result = []
		for letter in trie["children"]:
			temp = traverse(trie["children"][letter], words, prefix+letter)
			for suf in temp:
				result.append(letter + suf)
				if trie["children"][letter]["frequency"] != 0:
					words[prefix+letter] = trie["children"][letter]["frequency"]
		return result

def contains_prefix(word, prefix):
	if len(prefix) > len(word):
		return False
	for i in range(len(prefix)):
		if prefix[i] != word[i]:
			return False
	return True

def autocomplete(trie, prefix, N):
	words = all_words(trie)
	ans = {}
	for word in words:
		if contains_prefix(word, prefix):
			ans[word] = words[word]

	ans = sorted(ans, key=ans.get)
	ans.reverse()

	if len(ans) <= N:
		return ans
	else:
		return ans[:N]

alphabet = "abcdefghijklmnopqrstuvwxyz"

def two_character_transpose(word):
	words = {}
	for i in range(len(word)):
		for j in range(len(word)):
			if i < j:
				new = word[:i] + word[j] + word[i+1:j] + word[i] + word[j+1:]
				if new not in words:
					words[new] = 1
	return words.keys()


def valid_edits(prefix, words):
	edits = {}
	for i in range(len(prefix)+1):
		for letter in alphabet:
			word = prefix[:i] + letter + prefix[i:]
			if word in words:
				edits[word] = words[word]
			if i != len(prefix):
				word = prefix[:i] + letter + prefix[i+1:]
				if word in words and word not in edits:
					edits[word] = words[word]
		if i != len(prefix):
			word = prefix[:i] + prefix[i+1:]
			if word in words and word not in edits:
				edits[word] = words[word]

	for word in two_character_transpose(prefix):
		if word in words and word not in edits:
			edits[word] = words[word]

	return edits


def autocorrect(trie, prefix, N):
	words = all_words(trie)
	answer = autocomplete(trie, prefix, N)
	if len(answer) >= N:
		return answer
	
	C = N - len(answer)
	edits = valid_edits(prefix, words)
	edits = sorted(edits, key=edits.get)
	edits.reverse()

	possible = []
	for edit in edits:
		if edit not in answer:
			possible.append(edit)

	return answer + possible[:C]













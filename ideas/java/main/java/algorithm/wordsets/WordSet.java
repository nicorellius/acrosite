package algorithm.wordsets;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;

import algorithm.Word;

public abstract class WordSet {
	
	Map<Character, List<Word>> alphabetizedDictionary = new HashMap<Character, List<Word>>();
	
	public abstract Set<Word> getCompleteListOfWords();
	public Set<Word> allWords;
		
	public List<Word> getByFirstLetter(char firstLetter){
		if (alphabetizedDictionary.size() == 0){
			buildMap();
		}
		return alphabetizedDictionary.get(firstLetter);
	}
	
	public void buildMap(){
		for (Word w : allWords){
			char firstLetter = w.getWord().charAt(0);
			List<Word> words = new ArrayList<Word>();
			words.add(w);
			if (alphabetizedDictionary.get(firstLetter) != null){
				words.addAll(alphabetizedDictionary.get(firstLetter));
			}
			alphabetizedDictionary.put(firstLetter, words);
		}
	}
}

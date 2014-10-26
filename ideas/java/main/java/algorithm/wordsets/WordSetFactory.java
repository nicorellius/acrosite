package algorithm.wordsets;

import algorithm.Word;

import java.util.HashSet;
import java.util.Set;

public class WordSetFactory {

	public static ComplexWordSet mergeWordSets(Set<WordSet> wordsets){
		
		Set<Word> allWords = new HashSet<Word>();
		
		for (WordSet w : wordsets){
			w.getCompleteListOfWords();
			allWords.addAll(w.getCompleteListOfWords());
		}
		
		ComplexWordSet cws = new ComplexWordSet(allWords);
		cws.buildMap();
		return cws;
	}
}

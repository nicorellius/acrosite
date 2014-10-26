package algorithm.wordsets;

import java.util.Set;

import algorithm.Word;

public class ComplexWordSet extends WordSet{

	
	public ComplexWordSet(Set<Word> completeListOfWords){
		allWords = completeListOfWords;
	}
	
	@Override
	public Set<Word> getCompleteListOfWords() {
		return allWords;
	}

}

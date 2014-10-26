package algorithm.wordsets;

import java.util.HashSet;
import java.util.Set;

import algorithm.Word;

public class FunnyWords extends WordSet{

	@Override
	public Set<Word> getCompleteListOfWords() {
		HashSet<Word> allwords = new HashSet<Word>();

		allwords.add(new Word("shit","noun",1));
		return allwords;
	}

}

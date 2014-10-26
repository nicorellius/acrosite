package algorithm.wordsets;

import java.util.HashSet;
import java.util.Set;

import algorithm.Word;
import algorithm.WordAttributes;

public class DaysOfTheWeek extends WordSet{

	@Override
	public Set<Word> getCompleteListOfWords() {
		HashSet<Word> allwords = new HashSet<Word>();
		WordAttributes A = new WordAttributes();
		A.setPartOfSpeech("noun");
		A.setNumSyllables(2);
		A.addTag("dayoftheweek");

		allwords.add(new Word("monday",A));
		allwords.add(new Word("tuesday",A));
		allwords.add(new Word("wednesday",A));
		allwords.add(new Word("thursday",A));
		allwords.add(new Word("friday",A));
		allwords.add(new Word("sunday",A));
		
		Word sat = new Word("saturday","noun",3);
		sat.getAttributes().addTag("dayoftheweek");
		allwords.add(sat);
		allWords = allwords;
		return allwords;
	}
}

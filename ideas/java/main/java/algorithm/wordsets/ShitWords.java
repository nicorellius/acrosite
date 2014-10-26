package algorithm.wordsets;

import java.util.HashSet;
import java.util.Set;

import algorithm.Word;

public class ShitWords extends WordSet{

	@Override
	public Set<Word> getCompleteListOfWords() {
		HashSet<Word> allwords = new HashSet<Word>();

		//S
		allwords.add(new Word("So","conjunction",1));
		allwords.add(new Word("Sincerely","adverb",1));
//		allwords.add(new Word("Simply"));
//		allwords.add("Stunningly");;
//		allwords.add("Stupidly");
		
		//H
		allwords.add(new Word("Happy","adjective",2));
//		allwords.add("Hungry");
//		allwords.add("Hopeful");
//		allwords.add("Heroine-addicted");
//		allwords.add("Handsome");
		
		//I
		allwords.add(new Word("It's","contraction",1));
//		allwords.add("I'm");
//		allwords.add("I'm wanting");
//		allwords.add("If it's");
		
		//T
//		allwords.add("Tuesday");
		allwords.add(new Word("Thursday","noun",2));
//		allwords.add("Thanksgiving");
//		allwords.add("Tired");
		
		return allwords;
	}

}

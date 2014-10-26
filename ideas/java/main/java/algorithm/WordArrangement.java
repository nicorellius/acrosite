package algorithm;

import algorithm.wordsets.WordSet;

public interface WordArrangement {

	public WordArrangement generateWordArrangement(WordSet dictionary, WordSet hiddenMessageSet);
}

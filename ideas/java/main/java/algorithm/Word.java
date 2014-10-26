package algorithm;

public class Word {

	String word;
	WordAttributes attributes;
	
	public Word(String word, WordAttributes attributes){
		this.word = word;
		this.attributes = attributes;
	}
	
	public Word(String word, String partOfSpeech, int numSyllables){
		this(word, new WordAttributes(partOfSpeech, numSyllables));
	}
	
	public String getWord() {
		return word;
	}
	public void setWord(String word) {
		this.word = word;
	}
	public WordAttributes getAttributes() {
		return attributes;
	}
	public void setAttributes(WordAttributes attributes) {
		this.attributes = attributes;
	}

}

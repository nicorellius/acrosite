package algorithm;

import java.util.HashSet;
import java.util.Set;

public class WordAttributes {

	int numSyllables;
	String partOfSpeech;
	Set<String> tags = new HashSet<String>();
	
	public WordAttributes(){
		
	}
	
	public WordAttributes(String partOfSpeech, int NumSyllables){
		this.partOfSpeech = partOfSpeech;
		this.numSyllables = NumSyllables;
	}

	public void addTag(String tag){
		tags.add(tag);
	}
	
	public String getPartOfSpeech() {
		return partOfSpeech;
	}

	public void setPartOfSpeech(String partOfSpeech) {
		this.partOfSpeech = partOfSpeech;
	}

	public int getNumSyllables() {
		return numSyllables;
	}

	public void setNumSyllables(int numSyllables) {
		this.numSyllables = numSyllables;
	}

	public Set<String> getTags() {
		return tags;
	}

	public void setTags(Set<String> tags) {
		this.tags = tags;
	}
}

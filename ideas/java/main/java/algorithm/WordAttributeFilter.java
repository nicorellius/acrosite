package algorithm;

import java.util.Map;
import java.util.Map.Entry;

public class WordAttributeFilter {

	Map<String,Object> ExactMatches;
	Map<String,Object> PartialMatches;
	
	public boolean passesFilter(Word W){
		for (Entry<String, Object> entry : ExactMatches.entrySet()){
			String category = entry.getKey();
			Object value = entry.getValue();
			
			if (category.equals("word")){
				if (!value.equals(W.getWord())){
					return false;
				}
			} else if (category.equals("partOfSpeech")){
				if (!value.equals(W.getAttributes().getPartOfSpeech())){
					return false;
				}
			}
		}
		
		return true;
	}

	public Map<String, Object> getExactMatches() {
		return ExactMatches;
	}

	public void setExactMatches(Map<String, Object> exactMatches) {
		ExactMatches = exactMatches;
	}
}

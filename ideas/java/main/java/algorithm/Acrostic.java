package algorithm;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import algorithm.wordsets.WordSet;


public class Acrostic implements WordArrangement{

	@Override
	public WordArrangement generateWordArrangement(WordSet dictionary,
			WordSet hiddenMessageSet) {
		// TODO Auto-generated method stub
		return null;
	}
	
	public static List<String> getRandomAcrostic(char[] word, WordSet Dictionary, List<WordAttributeFilter> filters){
		
		List<String> acrostic = new ArrayList<String>();
		
		for (int i = 0; i < word.length; i++){
			char c = word[i];
			WordAttributeFilter WAF = filters.get(i);
			boolean keepSearching = true;
			while (keepSearching) {
				List<Word> acceptableWords = Dictionary.getByFirstLetter(c);
				Random r = new Random();
				int Index = Math.abs(r.nextInt() % acceptableWords.size());
				Word w = acceptableWords.get(Index);
				if (!acrostic.contains(w.getWord()) &&
						WAF.passesFilter(w)){
					acrostic.add(w.getWord());
					keepSearching = false;
				}
			}
		}
		
		return acrostic;
	}
	
	public static String printAcrosticText(List<String> acrosticText){
		StringBuilder sb = new StringBuilder();
		for (String word: acrosticText){
			sb.append(word.substring(0, 1).toUpperCase());
			sb.append(word.substring(1, word.length()));
			sb.append(System.getProperty("line.separator"));
		}
		return sb.toString();
	}

}

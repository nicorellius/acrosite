package algorithm.wordsets;

import algorithm.Word;
import algorithm.WordAttributes;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.HashSet;
import java.util.Set;

public class NegativeAdjectives extends WordSet{

	@Override
	public Set<Word> getCompleteListOfWords() {
		
		/*
		 * From
		 * https://www.englishclub.com/vocabulary/adjectives-personality-negative.htm
		 */
		
		String[] wordsThemselves = new String[]{
				"aggressive",
				"aloof",
				"arrogant",
				"belligerent",
				"big-headed",
				"bitchy",
				"boastful",
				"bone-idle",
				"boring",
				"bossy",
				"callous",
				"cantankerous",
				"careless",
				"changeable",
				"clinging",
				"compulsive",
				"conservative",
				"cowardly",
				"cruel",
				"cunning",
				"cynical",
				"deceitful",
				"detached",
				"dishonest",
				"dogmatic",
				"domineering",
				"finicky",
				"flirtatious",
				"foolish",
				"foolhardy",
				"fussy",
				"greedy",
				"grumpy",
				"gullible",
				"harsh",
				"impatient",
				"impolite",
				"impulsive",
				"inconsiderate",
				"inconsistent",
				"indecisive",
				"indiscreet",
				"inflexible",
				"interfering",
				"intolerant",
				"irresponsible",
				"jealous",
				"lazy",
				"machiavellian",
				"materialistic",
				"mean",
				"miserly",
				"moody",
				"narrow-minded",
				"nasty",
				"naughty",
				"nervous",
				"obsessive",
				"obstinate",
				"overcritical",
				"overemotional",
				"parsimonious",
				"patronizing",
				"perverse",
				"pessimistic",
				"pompous",
				"possessive",
				"pusillanimous",
				"quarrelsome",
				"quick-tempered",
				"resentful",
				"rude",
				"ruthless",
				"sarcastic",
				"secretive",
				"selfish",
				"self-centred",
				"self-indulgent",
				"silly",
				"sneaky",
				"stingy",
				"stubborn",
				"stupid",
				"superficial",
				"tactless",
				"timid",
				"touchy",
				"thoughtless",
				"truculent",
				"unkind",
				"unpredictable",
				"unreliable",
				"untidy",
				"untrustworthy",
				"vague",
				"vain",
				"vengeful",
				"vulgar",
				"weak-willed"
		};
 		
		WordAttributes A = new WordAttributes();
		A.setPartOfSpeech("adjective");
		A.addTag("negative");
		
		HashSet<Word> allwords = new HashSet<Word>();
		for (String s : wordsThemselves){
			allwords.add(new Word(s,A));
		}
		allWords = allwords;
		return allwords;
	}

	
	public static void main(String args[]){
		String file = "/Users/phillipseitzer/EclipseProjects/acrosticshirts/top100NegativeAdjectives.txt";
		try {
			BufferedReader br = new BufferedReader(new FileReader(file));
			String line = null;
			while ((line = br.readLine()) != null){
				System.out.println("\"" + line.trim() +"\",");
			}
			br.close();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}

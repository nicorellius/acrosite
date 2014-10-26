package algorithm.wordsets;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.HashSet;
import java.util.Set;

import algorithm.Word;
import algorithm.WordAttributes;

public class CommonNouns extends WordSet{

	@Override
	public Set<Word> getCompleteListOfWords() {
		/*
		 * From http://www.espressoenglish.net/100-common-nouns-in-english/
		 */
		String[] wordsThemselves = new String[]{
				"asshole",
				"time",
				"year",
				"people",
				"way",
				"day",
				"man",
				"thing",
				"woman",
				"life",
				"child",
				"world",
				"school",
				"state",
				"family",
				"student",
				"group",
				"country",
				"problem",
				"hand",
				"part",
				"place",
				"case",
				"week",
				"company",
				"system",
				"program",
				"question",
				"work",
				"government",
				"number",
				"night",
				"point",
				"home",
				"water",
				"room",
				"mother",
				"area",
				"money",
				"story",
				"fact",
				"month",
				"lot",
				"right",
				"study",
				"book",
				"eye",
				"job",
				"word",
				"business",
				"issue",
				"side",
				"kind",
				"head",
				"house",
				"service",
				"friend",
				"father",
				"power",
				"hour",
				"game",
				"line",
				"end",
				"member",
				"law",
				"car",
				"city",
				"community",
				"name",
				"president",
				"team",
				"minute",
				"idea",
				"kid",
				"body",
				"information",
				"back",
				"parent",
				"face",
				"others",
				"level",
				"office",
				"door",
				"health",
				"person",
				"art",
				"war",
				"history",
				"party",
				"result",
				"change",
				"morning",
				"reason",
				"research",
				"girl",
				"guy",
				"moment",
				"air",
				"teacher",
				"force",
				"education",
				"hack"
		};
 		
		WordAttributes A = new WordAttributes();
		A.setPartOfSpeech("noun");
		A.addTag("top100common");
		
		HashSet<Word> allwords = new HashSet<Word>();
		for (String s : wordsThemselves){
			allwords.add(new Word(s,A));
		}
		allWords = allwords;
		return allwords;
	}

	
	
	public static void main(String args[]){
		String file = "/Users/phillipseitzer/EclipseProjects/acrosticshirts/top100CommonNouns.txt";
		try {
			BufferedReader br = new BufferedReader(new FileReader(file));
			String line = null;
			while ((line = br.readLine()) != null){
				String[] L = line.trim().split("\\s+");
				System.out.println("\"" + L[1] +"\",");
			}
			br.close();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}

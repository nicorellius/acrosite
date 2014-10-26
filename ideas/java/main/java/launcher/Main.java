package launcher;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

import gui.AcrosticShirtsFrame;

import javax.swing.SwingUtilities;

import algorithm.Acrostic;
import algorithm.WordAttributeFilter;
import algorithm.wordsets.CommonNouns;
import algorithm.wordsets.ComplexWordSet;
import algorithm.wordsets.NegativeAdjectives;
import algorithm.wordsets.ShitWords;
import algorithm.wordsets.WordSet;
import algorithm.wordsets.WordSetFactory;

public class Main {

	public static void main(String[] args){
		if (args.length != 0){
			//launch the GUI
			
			SwingUtilities.invokeLater(new Runnable() {
				@Override
				public void run() {
					new AcrosticShirtsFrame();
				}
			});
		} else {
//			//Testing
//			ShitWords sh = new ShitWords();
//			sh.buildMap();
//			for (int i = 0; i < 10; i++){
//				String msg = Acrostic.printAcrosticText(Acrostic.getRandomAcrostic("SHIT".toCharArray(), sh));
//				System.out.println(msg);
//			}
			
//			/**
//			 * Test: Saturday, October 4
//			 */
//			CommonNouns na = new CommonNouns();
//			na.buildMap();
//			for (int i = 0; i < 10; i++){
//			String msg = Acrostic.printAcrosticText(Acrostic.getRandomAcrostic("shopping".toCharArray(), na));
//			System.out.println(msg);
//			}
			
			Set<WordSet> sets = new HashSet<WordSet>();
			sets.add(new CommonNouns());
			sets.add(new NegativeAdjectives());
			ComplexWordSet cws = WordSetFactory.mergeWordSets(sets);
						
			String keyword = "bush";
			List<WordAttributeFilter> filters = new ArrayList<WordAttributeFilter>();
			for (int i = 0; i < keyword.length(); i++){
				WordAttributeFilter WAF = new WordAttributeFilter();
				Map<String, Object> exactMatches = new HashMap<String, Object>();
				if (i < (keyword.length()-1)){
					exactMatches.put("partOfSpeech","adjective");
				} else {
					exactMatches.put("word","hack");
					//exactMatches.put("partOfSpeech","noun");
				}
				WAF.setExactMatches(exactMatches);
				filters.add(WAF);
			}
			
			for (int i = 0; i < 10; i++){
				String msg = Acrostic.printAcrosticText(Acrostic.getRandomAcrostic(keyword.toCharArray(), cws, filters));
				System.out.println(msg);
			}
		}
	}
}

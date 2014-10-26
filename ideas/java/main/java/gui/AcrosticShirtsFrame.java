package gui;

import java.awt.Dimension;

import javax.swing.JFrame;

public class AcrosticShirtsFrame extends JFrame{
	
	private static final long serialVersionUID = 1L;

	public AcrosticShirtsFrame(){

		getPanels();
		getFrame();
		
		this.setVisible(true);
	}
	
	public void getFrame(){
		this.setSize(new Dimension(500,500));
		this.setTitle("Acrostic T-shirts generator (version 1.0)");
		this.setLocationRelativeTo(null);
	}
	
	public void getPanels(){
		
	}
}

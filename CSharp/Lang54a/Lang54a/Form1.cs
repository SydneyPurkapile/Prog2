namespace Lang54a
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            int miles = 0;
            int gallons = 0;
            double mpg = 0;

            if (comboBox1.Text == "1970 VW Bug")
            {
                miles = 286;
                gallons = 9;
            }
            else if (comboBox1.Text == "1979 Firebird")
            {
                miles = 412;
                gallons = 40;
            }
            else if (comboBox1.Text == "1980 Subaru")
            {
                miles = 361;
                gallons = 18;
            }
            else if (comboBox1.Text == "1975 Cutlass")
            {
                miles = 161;
                gallons = 11;
            }
            else
            {
                MessageBox.Show("Invalid Car Selection!");
                return;
            }

            mpg = (double)miles / gallons;
            mpg = Math.Round(mpg, 3);
            label4.Text = miles.ToString();
            label5.Text = gallons.ToString();
            label6.Text = mpg.ToString();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            label4.Text = "";
            label5.Text = "";
            label6.Text = "";
            comboBox1.Text = "";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}

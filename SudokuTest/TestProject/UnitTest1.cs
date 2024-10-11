using ConsoleApp1;

namespace TestProject
{
    public class UnitTest1
    {
        [Fact]
        public void Test1()
        {
            GradeSudoku obj = new(3);

            //obj.grade[0, 0] = 5;
            
            Assert.True(valida(obj));
        }

        private bool valida(GradeSudoku obj)
        {
            for (int i = 0; i < obj.grade.Length; i++)
                for (int j = 0; j < obj.grade.Length; j++)
                {
                    if (obj.grade[i, j] != 0)
                    {
                        return true;
                    }
                }

            return false;

        }
    }

    
}
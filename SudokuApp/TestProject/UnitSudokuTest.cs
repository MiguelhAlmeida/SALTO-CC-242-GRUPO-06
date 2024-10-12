using SudokuApp;

namespace TestProject
{
    public class UnitSudokuTest
    {
        [Fact]
        public void Test1()
        {
            Sudoku obj = new(3);
            
            Assert.True(valida(obj));
        }

        private bool valida(Sudoku obj)
        {
            for (int i = 0; i < obj.Matriz.Length; i++)
                for (int j = 0; j < obj.Matriz.Length; j++)
                {
                    if (obj.Matriz[i, j] != 0)
                    {
                        return true;
                    }
                }

            return false;

        }
    }

    
}
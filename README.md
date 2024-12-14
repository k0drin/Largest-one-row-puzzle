# Digital puzzle

## Technical specifications
We need to make a digital puzzle where the connecting elements are the first or last TWO digits. To simplify the task, we will use a single-row puzzle where its fragments can be placed only one after the other.

For example, we have the following rows with numbers:

`608017, 248460, 962282, 994725, 177092`

So analyzing the final parts, we can make the following chain:

`248460 & 608017 & 177092 -> 2484(60)80(17)7092`

Thus, the largest sequence and the answer will be: `24846080177092`
 
The input text file has 142 fragments, which must consist only of numbers! Determine the largest (longest) sequence for these fragments.
And each fragment must be used only 1 time.

## The solution and its launch

1. Download Python 

    For [Windows](https://www.python.org/downloads/windows/)

    **Debian based**
    ```bash
    sudo apt update
    sudo apt install python3
    python --version

    ```
    **Arch based**
    ```bash
    sudo pacman -Syu
    sudo pacman -S python
    python --version
    ```

2. Download Git 

    For [Windows](https://git-scm.com/downloads/win)

    **Debian based**
    ```bash
    sudo apt install git
    git --version
    ```

    **Arch based**
    ```bash
    sudo pacman -S git
    git --version
    ```


3. **Clone the repository:**

    HTTP

    ```bash
    https://github.com/k0drin/Largest-one-row-puzzle.git
    ```
    SSH
    ```bash
    git@github.com:k0drin/Largest-one-row-puzzle.git
    ```

4. **Run the code**
    ```bash
    python3 main.py
    ```

5. **Expected output**
    ```bash
    Largest Sequence: 716890565777794373556482064083064121343222972497868721751153303887119612013153750510417085100512022142771171781184759586758823141707943693917372699031562942007148831088658432465190816374922650246027977309775416923314139340173379890062028614605676733227368753511935367493
    ```
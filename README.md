
# 🧩 The Great Code Off: Safe Coordinates Challenge

In a 2D grid world, a robot starts at coordinate (0, 0) and can move **only horizontally or vertically** one square at a time.

However, the world is dangerous:  
**any coordinate where the sum of the digits of the product of the x and y values is equal to or greater than 19 is mined.**

### For example:
- (3, 4) → 3×4 = 12 → 1+2 = 3 → ✅ Safe  
- (6, 9) → 6×9 = 54 → 5+4 = 9 → ✅ Safe  
- (96, -69) → 96×69 = 6624 → 6+6+2+4 = 18 → ✅ Safe  
- (67, 43) → 67×43 = 2881 → 2+8+8+1 = 19 → 💣 Mined
- (123, 456) → 123×456 = 56088 → 5+6+0+8+8 = 27 → 💣 Mined  

---

## 🧠 Functions to Implement

### `boolean isSafe(int x, int y)`
Checks if a coordinate is safe to visit.

**Parameters:**
- `x` (int): x-coordinate  
- `y` (int): y-coordinate  

**Returns:**
- `true` if the sum of the digits of (x × y) is < 19  
- `false` otherwise

---

### `int totalSafeSquares()`
Calculates the total number of safe squares the robot can reach from (0, 0), using only horizontal and vertical moves.

**Returns:**
- The number of reachable safe squares

---

### `int shortestSafeJourney(int a, int b, int x, int y)` _(Extension Task)_
Finds the shortest safe path from (a, b) to (x, y), if one exists.

**Parameters:**
- `a`, `b`: starting coordinates  
- `x`, `y`: destination coordinates  

**Returns:**
- The number of steps in the shortest safe path  
- `-1` if no safe path exists

---

## 🏆 Prizes

There are **two prizes** available:

### 🥇 Fastest Correct Answer
Awarded to the team that submits a correct and efficient solution to `totalSafeSquares()` in the shortest time.

**Why we should win this prize:**  

Our team implemented an efficient breadth-first search (BFS) algorithm for totalSafeSquares(), ensuring that every reachable safe square from (0, 0) is counted exactly once. We optimized our solution by:

- Using a queue and a set for fast lookups and minimal memory overhead.
- Avoiding unnecessary recalculations by checking each coordinate only once.
- Implementing a digit sum check that works efficiently for both positive and negative coordinates.
- Setting a practical boundary to prevent infinite search, while ensuring all reachable safe squares are included.
- Our code is clear, well-documented, and runs quickly even for large search areas. This efficiency and correctness make our solution stand out for the Fastest Correct Answer prize.
- As not being developers, we quickly got up to speed with the competition and used Github Copilot to assist us with creating each function and developing any ongoing documentation with comments. 
- Leveraged Github Copilot to generate the skeleton to our code and functions.
---

### 🧠 Most Unique Solution
Awarded to the team with the most creative, elegant, or unconventional approach to solving `shortestSafeJourney()`.

**Why we should win this prize:**  

Our solution to shortestSafeJourney() stands out for its clarity, adaptability, and user-friendliness. We implemented a classic breadth-first search (BFS) algorithm, but made it uniquely robust by:

- Designing the code to handle both positive and negative coordinates seamlessly, ensuring the robot can traverse the entire grid in any direction.
- Structuring our BFS to return the shortest path efficiently, even in the presence of complex "mined" regions, without unnecessary computation.
- Keeping the implementation highly readable and well-commented, making it accessible to both experienced developers and newcomers.
- Leveraging GitHub Copilot to accelerate our development and encourage collaborative, AI-assisted problem-solving—a modern and creative twist.
- Prioritizing code maintainability and extensibility, so future teams can easily adapt or enhance our approach.
-This blend of classic algorithm, modern AI assistance, and a focus on accessibility makes our solution both effective and uniquely creative
---

## ✍️ Team Write-Up

**Team Name:**  Team 5 - The AI Native/Low code team

**Team Members:**  Jamie Moxon, Urszula Piotrkowicz

**Approach Summary:**  
We approached the Safe Coordinates Challenge by focusing on clarity, efficiency, and leveraging modern AI tools. For both **totalSafeSquares()** and **shortestSafeJourney()**, we used a breadth-first search (BFS) algorithm, which is well-suited for exploring grids and finding shortest paths. Our implementation ensures that each coordinate is checked only once, using a set for visited positions and a queue for efficient traversal.

To handle the "mined" squares, we created an **isSafe(x, y)** function that quickly determines if a coordinate is safe by calculating the digit sum of the product of x and y. We made sure this works for both positive and negative coordinates.

Recognising the potential for infinite search in an unbounded grid, we introduced a practical boundary **(max_dist)** to ensure the algorithm completes efficiently while still covering all reachable safe squares.

Throughout development, we used GitHub Copilot to accelerate coding, generate function skeletons, and improve documentation. This allowed us to quickly iterate, test, and refine our solution, even as a team with limited traditional development experience.

Our code is modular, well-commented, and designed for easy understanding and extension. This approach allowed us to deliver a robust, efficient, and creative solution to the challenge.


---

## 📬 Submission Instructions

1. **Fork the official challenge repository.**  
2. Add your solution and team write-up to your fork.  
3. **Before the deadline, share your forked repository with the judges**
4. Ensure your code is well-documented and easy to run.
5. answer form for totalSafeSquares: https://forms.office.com/e/T90mYcnF1r
6. feedback from: https://forms.office.com/e/ewqSbUq593

---

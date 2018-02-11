from json import dumps


def validate(data=None):
    if not isinstance(data, list):
        raise Exception('Must provide grid')
    if len(data) != 10:
        raise Exception('Grid must contain 10 rows')
    for row in data:
        if len(row) != 10:
            raise Exception('Grid row must contain 10 cells')


class Blob():
    def __init__(self, data):
        validate(data)

        self.grid = data
        self.boundaries = {
            'Cell_Reads': 0,
            'Top': 10,
            'Left': 10,
            'Bottom': 0,
            'Right': 0,
        }

        self.cells_visited = {}
        self.find_boundaries()

    def find_boundaries(self):
        # Loop through until top edge of the blob is found
        cell = self._findFirstCell()

        # Set the top boundary
        self.boundaries['Top'] = cell['x']

        """
         From that cell keep going through checking
         the adjacent cells, and recording the outer limits
         until the outer edges of the blob are reached
        """
        self._check_adjacents(cell['x'], cell['y'])

    def _findFirstCell(self):
        cell = {'x': None, 'y': None}

        for i in range(0, 10):
            row = self.grid[i]
            for j in range(0, 10):
                _cell = row[j]
                if _cell == 1:
                    cell['x'] = i
                    cell['y'] = j
                    return cell
                else:
                    self._addToCellsVisited(i, j)

        raise Exception('Grid does not contain blob')

    def _addToCellsVisited(self, x, y):
        key = '{}{}'.format(x, y)
        self.cells_visited[key] = True

    def _check_adjacents(self, x, y):
        # if right is further right than ever before update
        if (y > self.boundaries['Right']):
            self.boundaries['Right'] = y
        # if left is further left than ever before update
        if (y < self.boundaries['Left']):
            self.boundaries['Left'] = y
        # if down is further down than ever before update
        if (x > self.boundaries['Bottom']):
            self.boundaries['Bottom'] = x

        # Keep checking the cells to right, left and below the
        # current cell if you hit hit a zero stop.
        self._process_cell(x, y + 1, 'right')
        self._process_cell(x, y - 1, 'left')
        self._process_cell(x + 1, y, 'down')

    def _process_cell(self, x, y, direction):
        # If the x,y coordinates fall outside the grid, return
        if (y >= len(self.grid) or x >= len(self.grid)):
            return
        if (y < 0):
            return

        if (self._was_visited(x, y) is False):
            # Read cell value and increase read count
            cell = self.grid[x][y]
            self.boundaries['Cell_Reads'] += 1
            self._addToCellsVisited(x, y)

            if (cell != 0):
                self._check_adjacents(x, y)

    def _was_visited(self, x, y):
        key = '{}{}'.format(x, y)
        return key in self.cells_visited

    def __str__(self):
        return dumps(self.boundaries)

import matplotlib.pypplot


class BinTreePlot:
    """plot a binary tree"""

    def __init__(self, bin_tree=None):
        """set up a node """
        self.bin_tree = bin_tree

    def get_coord(coord_prt, depth_le, depth, child_type="left"):
        if child_type == "left":
            x_child = coord_prt[0] - 1 / (2 ** (depth_le + 1))
        elif child_type == "right":
            x_child = coord_prt[0] + 1 / (2 ** (depth_le + 1))
        else:
            raise Exception("No other child type")
        y_child = coord_prt[1] - 1 / depth
        return x_child, y_child

    def plot_node(ax, node_text, center_point, parent_point):
        ax.annotate(node_text, xy=parent_point,  xycoords='axes fraction', xytext=center_point, textcoords='axes fraction',
                va="bottom", ha="center", bbox=NODE_STYLE, arrowprops=ARROW_ARGS)

    def get_leaf_num(self):
        """method of getting leaf numbers of BiTree"""
        if self.root is None:
            return 0
        else:
            node_stack = list()
            node = self.root
            leaf_numbers = 0
            # only node exists and stack is not empty that will do this circulation
            while node is not None or len(node_stack):
                if node is None:
                    """node is None then pop the stack and get the node.right"""
                    node = node_stack.pop().right
                    continue
                while node.left is not None:
                    node_stack.append(node)
                    node = node.left
                # if there is not  node.right, leaf_number add 1
                node = node.right
                if node is None:
                    leaf_numbers += 1
            return leaf_numbers

    def get_depth(self):
        """method of getting depth of BiTree"""
        if self.root is None:
            return 0
        node_queue = list()
        node_queue.append(self.root)
        depth = 0
        while len(node_queue):
            q_len = len(node_queue)
            while q_len:
                q_node = node_queue.pop(0)
                q_len = q_len - 1
                if q_node.left is not None:
                    node_queue.append(q_node.left)
                if q_node.right is not None:
                    node_queue.append(q_node.right)
            depth = depth + 1
        return depth

    def __init__(self, label='BinaryTree'):
        self.label = label

    def draw_init(self):
        fig = plt.figure(self.label, figsize=(16, 12))
        ax = fig.add_subplot(111)
        return ax

    def show(self):
        plt.show()

    def view_in_graph(self):
        """use matplotlib.pypplot to help view the BiTree """

        if self.root is None:
            print("An Empty Tree, Nothing to plot")
            return
        depth = self.get_depth()
        ax = node_plot.draw_init()
        coord0 = (1 / 2, 1 - 1 / (2 * depth))
        node_queue = list()
        coord_queue = list()
        node_plot.plot_node(ax, str(self.root.get_element()), coord0, coord0)
        node_queue.append(self.root)
        coord_queue.append(coord0)
        cur_level = 0
        while len(node_queue):
            q_len = len(node_queue)
            while q_len:
                q_node = node_queue.pop(0)
                coord_prt = coord_queue.pop(0)
                q_len = q_len - 1
                if q_node.left is not None:
                    xc, yc = node_plot.get_coord(coord_prt, cur_level + 1, depth, "left")
                    element = str(q_node.left.get_element())
                    node_plot.plot_node(ax, element, (xc, yc), coord_prt)
                    node_queue.append(q_node.left)
                    coord_queue.append((xc, yc))
                if q_node.right is not None:
                    xc, yc = node_plot.get_coord(coord_prt, cur_level + 1, depth, "right")
                    element = str(q_node.right.get_element())
                    node_plot.plot_node(ax, element, (xc, yc), coord_prt)
                    node_queue.append(q_node.right)
                    coord_queue.append((xc, yc))
            cur_level += 1
        node_plot.show()

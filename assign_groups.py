
import csv


class AssignGroups:
    def __init__(self, roster, group_size, num_groups, lab_num=0):
        self.roster = roster
        self.group_size = group_size
        self.num_groups = num_groups
        self.rand_seed = lab_num
        self._get_names_from_roster()
        self.target_group_size = len(self.names) / num_groups

    def _get_names_from_roster(self):
        reader = csv.reader(self.roster)
        self.names = []
        for line in reader:
            self.names.append(line[1])

    def assign_groups(self):
        pass
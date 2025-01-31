from oelint_adv.cls_rule import Rule
from oelint_parser.cls_item import Variable


class VarDescSameTooBrief(Rule):
    def __init__(self):
        super().__init__(id='oelint.vars.descriptiontoobrief',
                         severity='warning',
                         message='\'DESCRIPTION\' is the shorter than \'SUMMARY\'')

    def check(self, _file, stash):
        res = []
        items = stash.GetItemsFor(filename=_file, classifier=Variable.CLASSIFIER,
                                  attribute=Variable.ATTR_VAR, attributeValue='DESCRIPTION')
        items_sum = stash.GetItemsFor(filename=_file, classifier=Variable.CLASSIFIER,
                                      attribute=Variable.ATTR_VAR, attributeValue='SUMMARY')
        for i in items:
            _same = [x for x in items_sum if len(
                x.VarValueStripped) > len(i.VarValueStripped)]
            if any(_same):
                res += self.finding(i.Origin, i.InFileLine)
        return res

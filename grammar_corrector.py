import language_tool_python as ltp

class Corrector:

    def correct_text(text):
        tool = ltp.LanguageTool('en-IN')
        matches = tool.check(text)

        mistakes=[]
        corrections=[]
        start_pos=[]
        end_pos=[]

        for rules in matches:
            if len(rules.replacements)>0:
                start_pos.append(rules.offset)
                end_pos.append(rules.errorLength + rules.offset)
                mistakes.append(text[rules.offset:rules.errorLength + rules.offset])
                corrections.append(rules.replacements[0])

        corrected_text=list(text)
        for i in range(len(start_pos)):
            for j in range(len(text)):
                corrected_text[start_pos[i]]=corrections[i]
                if j>start_pos[i] and j<end_pos[i]:
                    corrected_text[j]=''

        corrected_text = ''.join(corrected_text)

        return corrected_text


if __name__=='__main__':
    print("you is a good boy")
    c = Corrector()
    res=c.correct_text("You is a good boy")

    print(res)

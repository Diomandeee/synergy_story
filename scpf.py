import openai
import json


class SynergisticPrompt:

    def __init__(self, open_ai_api_key, model_engine = "text-davinci-003", prompt_idea = None):
        """
        :param model_engine: the GPT-3 model engine to use
        :param prompt_idea: the initial prompt idea to use
        """

        self.model_engine = model_engine
        self.prompt_idea = prompt_idea
        self.open_ai_api_key = open_ai_api_key
        openai.api_key = self.open_ai_api_key


    def generate_ideas(self, topic, colors, textures):
        """
        Generates ideas for a scene using brainstorming and GPT-3.

        :param topic: the topic, genre, or theme for the scene
        :param colors: colors or textures to be included in the scene
        :param textures: colors or textures to be included in the scene
        :return: a list of potential elements or themes for the scene
        """
        technique_desc = "To generate ideas for the scene, let's use the brainstorming technique Non Linear Navigation. Just as the universe is non-linear and complex, so too can our thoughts and solutions. Embrace the chaos and navigate through the unknown."
        prompt = technique_desc + "\n\nBrainstorm ideas for a " + topic + " scene with a mix of " + colors + " and " + textures + "."
        response = openai.Completion.create(engine=self.model_engine, prompt=prompt, max_tokens=1000, n=1, stop=None, temperature=1)
        completions = response["choices"][0]["text"]
        self.prompt_idea = completions.strip()
    
        return completions
    

    def generate_questions(self):
        """
        Generates thought-provoking questions related to the generated ideas using GPT-3.

        :param ideas: a list of ideas generated from the previous step
        :return: a list of thought-provoking questions related to the ideas
        """
        technique_desc = "To deepen our understanding of the scene and generate further ideas, let's use Metaphysical Illumination to create thought-provoking questions. Like a flash of lightning illuminating the night sky, we can seek deeper truths and insights by exploring the mysteries of existence."
        prompt = technique_desc + "\n\n" + str(self.prompt_idea)
        response = openai.Completion.create(engine=self.model_engine, prompt=prompt, max_tokens=1000, n=1, stop=None, temperature=1)
        completions = response["choices"][0]["text"]
        questions = completions.strip()
        return questions


    def generate_prompts(self, questions):
        """
        Generates specific prompts to capture all aspects from the brainstorming and questions using GPT-3.

        :param questions: a list of thought-provoking questions generated from the previous step
        :return: a list of detailed prompts related to the questions
        """
        prompt = "To create a detailed prompt for the scene, let's use Convergent Fusion to generate specific prompts that capture all aspects from the brainstorming and questions. Like a convergence of multiple streams, the following prompts are meant to be combined to create a synergetic prompt." + str(questions)
        response = openai.Completion.create(engine=self.model_engine, prompt=prompt, max_tokens=1000, n=1, stop=None, temperature=1)
        completions = response["choices"][0]["text"]
        prompts = completions.strip()
        return self.generate_synergetic_prompt(prompts)
    
    
    def generate_synergetic_prompt(self, prompts):
        """
        Generates a synergetic prompt using GPT-3
        
        :param prompts: a list of detailed prompts generated from the previous step
        :return: a synergetic prompt
        """
        technique_desc = "To create a synergetic prompt, let's use Convergent Fusion to combine the prompts into a single prompt. Like a convergence of multiple streams, the following prompt is meant to be used to generate a story."
        prompt = technique_desc + "\n\n" + str(prompts)
        response = openai.Completion.create(engine=self.model_engine, prompt=prompt, max_tokens=1000, n=1, stop=None, temperature=1)
        completions = response["choices"][0]["text"]
        synergetic_prompt = completions.strip()
        return synergetic_prompt
    

    def generate_story(self, synergetic_prompt):
        """
        Generates a story using the synergetic prompt
        
        :param synergetic_prompt: a synergetic prompt generated from the previous step
        :return: a story generated using the synergetic prompt
        """
        technique_desc = "To generate a story, let's use the brainstorming technique Non Linear Navigation. Just as the universe is non-linear and complex, so too can our thoughts and solutions. Embrace the chaos and navigate through the unknown."
        prompt = technique_desc + "\n\n" + str(synergetic_prompt)
        response = openai.Completion.create(engine=self.model_engine, prompt=prompt, max_tokens=3000, n=1, stop=None, temperature=1)
        completions = response["choices"][0]["text"]
        story = completions.strip()
        return story


    def run(self, topic, colors, textures):
        """
        Runs the SCPF prompt generation process
        :param topic: the topic, genre, or theme for the scene
        :param colors: colors or textures to be included in the scene
        :param textures: colors or textures to be included in the scene
        :return: a story generated using the synergetic prompt
        """
        ideas = self.generate_ideas(topic, colors, textures)
        questions = self.generate_questions()
        prompts = self.generate_prompts(questions)
        synergetic_prompt = self.generate_synergetic_prompt(prompts + "\n\n" + self.prompt_idea)
        story = self.generate_story(synergetic_prompt)
        


        response = {
            "ideas": ideas,
            "questions": questions,
            "synergetic_prompt": synergetic_prompt,
            "story": story
        }   
        
        # save the response to a json file
        
        with open('response.json', 'w') as f:
            json.dump(response, f , indent=4)

        return story


# Example Usage:

if __name__ == "__main__":
    API_KEY_4="sk-"

    # Create a SynergisticPrompt object
    prompt = SynergisticPrompt(open_ai_api_key=API_KEY_4)
    
    # Generate a story
    story = prompt.run("romance", "red", "silk")
    
    # Print the story
    print(story)
    

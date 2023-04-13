import openai
import json

    
class SynergisticPrompt_v1:

    def __init__(self, open_ai_api_key, model_engine = "text-davinci-003", prompt_idea = None):
        self.model_engine = model_engine
        self.prompt_idea = prompt_idea
        self.themes = None
        self.moods = None
        self.comp_light = None
        self.keywords = None
        self.ideas = None
        openai.api_key = open_ai_api_key


    def generate_prompt_idea(self):
        """
        This method generates the initial prompt idea either synthetically or taken from a txt file
        """
        if self.prompt_idea is None:
            prompt_idea = openai.Completion.create(
                engine=self.model_engine,
                prompt = "Red silk sheets draped across a king-size bed with feather-soft pillows. "
            )
            self.prompt_idea = prompt_idea.choices[0].text
        else:
            with open(self.prompt_idea, "r") as f:
                self.prompt_idea = f.read()


    def generate_themes(self):
        """
        This method generates a list of themes or stories based on the initial prompt idea
        """
        themes = openai.Completion.create(
            engine=self.model_engine,
            prompt=f"Based on the prompt idea: {self.prompt_idea}, generate a list of themes or stories.",
            max_tokens=500,
            temperature=1
        )
        self.themes = themes.choices[0].text


    def generate_moods(self):
        """
        This method generates a list of moods and atmospheres based on the initial prompt idea
        """
        moods = openai.Completion.create(
            engine=self.model_engine,
            prompt=f"Based on the prompt idea: {self.prompt_idea}, generate a list of moods and atmospheres.",
            max_tokens=500,
            temperature=1
        )
        self.moods = moods.choices[0].text


    def generate_composition_lighting(self):
        """
        This method generates a list of composition and lighting elements based on the initial prompt idea
        """
        comp_light = openai.Completion.create(
            engine=self.model_engine,
            prompt=f"Based on the prompt idea: {self.prompt_idea}, generate a list of composition and lighting elements.",
            max_tokens=500,
            temperature=1
        )
        self.comp_light = comp_light.choices[0].text


    def generate_keywords(self):
        """
        This method generates a list of keywords or phrases based on the initial prompt idea
        """
        keywords = openai.Completion.create(
            engine=self.model_engine,
            prompt=f"Based on the prompt idea: {self.prompt_idea}, generate a list of keywords or phrases.",
            max_tokens=500,
            temperature=1
        )
        self.keywords = keywords
        self.keywords = keywords.choices[0].text


    def generate_ideas(self):
        """
        This method generates a list of specific and detailed ideas based on the keywords or phrases generated in the previous method
        """
        ideas = openai.Completion.create(
            engine=self.model_engine,
            prompt=f"Based on the keywords or phrases: {self.keywords}, generate a list of specific and detailed ideas.",
            max_tokens=500,
            temperature=1
        )
        self.ideas = ideas.choices[0].text
        
        
    def generate_questions(self):
        """
        This method generates a list of  thought-provoking based on the ideas generated in the first stage
        """
        questions = openai.Completion.create(
            engine=self.model_engine,
            prompt=f"Given the following ideas: {self.ideas}, generate a list of thought-provoking that can guide the prompt creation process.",
            max_tokens=1024
        )
        self.questions = questions.choices[0].text


    def generate_prompts(self):
        """
        This method generates a list of specific prompts based on the open-ended questions from the previous stage
        """
        prompts = openai.Completion.create(
            engine=self.model_engine,
            # prompt = f"Create a prompt that captures the essence of the following question: {self.questions}"
            prompt=f"Given the following open-ended questions: {self.questions}, generate specific prompts.",
            max_tokens=1024
        )
        self.prompts = prompts.choices[0].text


    def generate_synergetic_prompt(self):
        """
        This method generates the synergetic prompt by combining the specific prompts from the previous stage
        """
        synergetic_prompt = openai.Completion.create(
            engine=self.model_engine,
            prompt=f"Given the following specific prompts: {self.prompts}, generate a synergetic prompt that captures all aspects of the desired image",
            max_tokens=1024
        )
        self.synergetic_prompt = synergetic_prompt.choices[0].text

        
    def generate_image(self):
        """
        This method generates the image based on the synergetic prompt
        """
        image = openai.Completion.create(
            engine=self.model_engine,
            prompt=f"Given the synergetic prompt: {self.synergetic_prompt}, generate the dalle-2 image prompt", 
            max_tokens=1024
        )
        self.image = image.choices[0].text
        
        
    def generate_image_description(self):
        """
        This method generates the image description based on the synergetic prompt
        """
        image_description = openai.Completion.create(
            engine=self.model_engine,
            prompt=f"Given the synergetic prompt: {self.synergetic_prompt}, generate the image description",
            max_tokens=1024
        )
        self.image_description = image_description.choices[0].text
        
        
    def generate_image_title(self):
        """
        This method generates the image title based on the synergetic prompt
        """
        image_title = openai.Completion.create(
            engine=self.model_engine,
            prompt=f"Given the synergetic prompt: {self.synergetic_prompt}, generate the image title",
            max_tokens=1024
        )
        self.image_title = image_title.choices[0].text
        
        
    def generate_image_caption(self):
        """
        This method generates the image caption based on the synergetic prompt
        """
        image_caption = openai.Completion.create(
            engine=self.model_engine,
            prompt=f"Given the synergetic prompt: {self.synergetic_prompt}, generate the image caption",
            max_tokens=1024
        )
        self.image_caption = image_caption.choices[0].text
        
        
    def generate_image_tags(self):
        """
        This method generates the image tags based on the synergetic prompt
        """
        image_tags = openai.Completion.create(
            engine=self.model_engine,
            prompt=f"Given the synergetic prompt: {self.synergetic_prompt}, generate the image tags",
            max_tokens=1024
        )
        self.image_tags = image_tags.choices[0].text
        
        
    def generate_image_metadata(self):
        """
        This method generates the image metadata based on the synergetic prompt
        """
        image_metadata = openai.Completion.create(
            engine=self.model_engine,
            prompt=f"Given the synergetic prompt: {self.synergetic_prompt}, generate the image metadata",
            max_tokens=1024
        )
        self.image_metadata = image_metadata.choices[0].text
        
        
    def generate_image_keywords(self):
        """
        This method generates the image keywords based on the synergetic prompt
        """
        image_keywords = openai.Completion.create(
            engine=self.model_engine,
            prompt=f"Given the synergetic prompt: {self.synergetic_prompt}, generate the image keywords",
            max_tokens=1024
        )
        self.image_keywords = image_keywords.choices[0].text
        

    def save_responses(self):
        """
        This method saves the responses from each phase in a separate file
        """   
        response = {
            "prompt_idea": self.prompt_idea,
            "themes": self.themes,
            "moods": self.moods,
            "comp_light": self.comp_light,
            "keywords": self.keywords,
            "ideas": self.ideas,
            "questions": self.questions,
            "prompts": self.prompts,
            "synergetic_prompt": self.synergetic_prompt,
            "image": self.image,
            "image_description": self.image_description,
            "image_title": self.image_title,
            "image_caption": self.image_caption,
            "image_tags": self.image_tags,
            "image_metadata": self.image_metadata,
            "image_keywords": self.image_keywords
        }
        with open("response_v1.json", "w") as f:
            json.dump(response, f, indent=4)
            
                
            
    def run(self):
        """
        This method calls all the other methods in the correct order
        """
        self.generate_prompt_idea()
        self.generate_themes()
        self.generate_moods()
        self.generate_composition_lighting()
        self.generate_keywords()
        self.generate_ideas()
        self.generate_questions()
        self.generate_prompts() 
        self.generate_synergetic_prompt()
        self.generate_image()
        self.generate_image_description()
        self.generate_image_title()
        self.generate_image_caption()
        self.generate_image_tags()
        self.generate_image_metadata()
        self.generate_image_keywords()
        self.save_responses()

        

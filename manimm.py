
from manim import *
from manim.utils.color import *

class AtomStructure(Scene):
    def construct(self):
        # Scene 1
        nucleus = Circle(radius=1, color=GREY, fill_opacity=1).add(Text("Nucleus", color=WHITE).scale(0.5))
        electron1 = Circle(radius=0.2, color=BLUE, fill_opacity=1).shift(2*RIGHT)
        electron2 = Circle(radius=0.2, color=BLUE, fill_opacity=1).shift(2*LEFT)
        electron_label = Text("Electrons", color=LIGHT_BLUE).scale(0.4).next_to(electron1, UP)
        electron1_path = Circle(radius=2, color=BLUE, stroke_width=0.5)
        electron2_path = Circle(radius=2, color=BLUE, stroke_width=0.5)

        self.play(FadeIn(nucleus))
        self.play(FadeIn(electron1), FadeIn(electron2), FadeIn(electron_label))
        self.play(MoveAlongPath(electron1, electron1_path), MoveAlongPath(electron2, electron2_path), run_time=3)
        self.wait(0.5)

        # Scene 2
        self.play(FadeOut(electron1), FadeOut(electron2), FadeOut(electron_label))
        self.play(nucleus.animate.scale(2))
        proton1 = Circle(radius=0.2, color=RED, fill_opacity=1).shift(0.5*RIGHT + 0.3*UP)
        proton2 = Circle(radius=0.2, color=RED, fill_opacity=1).shift(0.5*LEFT + 0.3*DOWN)
        neutron1 = Circle(radius=0.2, color=GREEN, fill_opacity=1).shift(0.5*LEFT + 0.3*UP)
        neutron2 = Circle(radius=0.2, color=GREEN, fill_opacity=1).shift(0.5*RIGHT + 0.3*DOWN)
        proton_label = Text("Protons", color=DARK_RED).scale(0.3).next_to(proton1, RIGHT)
        neutron_label = Text("Neutrons", color=DARK_GREEN).scale(0.3).next_to(neutron1, LEFT)

        self.play(FadeIn(proton1), FadeIn(proton2), FadeIn(neutron1), FadeIn(neutron2), 
                  FadeIn(proton_label), FadeIn(neutron_label))
        self.play(FadeOut(nucleus))

        self.wait(2)

if __name__ == '__main__':
    scene = AtomStructure()
    scene.render() 
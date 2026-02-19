from typing import Any
from django.core.management.base import BaseCommand
from blog.models import Post, Categories
import random

class Command(BaseCommand):
    help = "Create dummy blog Posts"

    def handle(self, *args: Any, **options: Any):
        Post.objects.all().delete()

        titles = [
            "The Future of AI",
            "Climate Change Solutions",
            "Remote Work Trends",
            "Quantum Computing Explained",
            "Renewable Energy Innovations",
            "Deep Learning Demystified",
            "Post-Pandemic Economic Outlook",
            "Blockchain in Finance",
            "Storytelling in Marketing",
            "Medical Technology Advances",
            "Space Exploration Challenges",
            "Psychology of Decision Making",
            "Evolution of Social Media",
            "The Art of Cooking",
            "Cultural Diversity in Society",
            "Sustainable Development Investments",
            "Globalization Impact",
            "Power of Mindfulness",
            "Online Learning Revolution",
            "Art and Technology Fusion",
        ]

        contents = [
            "Exploring the future of artificial intelligence and its impact on society...",
            "Discovering solutions to combat climate change and protect the environment...",
            "Analyzing trends and challenges in remote work environments...",
            "An introduction to the principles and applications of quantum computing...",
            "Investigating the latest innovations in renewable energy sources...",
            "Understanding the fundamentals of deep learning and neural networks...",
            "Examining the economic landscape in the aftermath of the COVID-19 pandemic...",
            "Exploring the potential of blockchain technology in the financial sector...",
            "Harnessing the power of storytelling to create compelling marketing campaigns...",
            "Highlighting breakthroughs and advancements in medical technology...",
            "Addressing the obstacles and opportunities in space exploration...",
            "Exploring the psychological factors influencing decision-making processes...",
            "Tracing the evolution of social media platforms and their impact on society...",
            "Celebrating the art of cooking and culinary creativity...",
            "Promoting inclusivity and embracing diversity in modern communities...",
            "Investigating sustainable development initiatives and their impact on the future...",
            "Examining the effects of globalization on local and global economies...",
            "Embracing mindfulness practices for enhanced well-being and productivity...",
            "Revolutionizing education through online learning platforms and resources...",
            "Exploring the intersection of art, design, and technology in the digital age...",
        ]

        img_urls = [
            f"https://picsum.photos/id/{i}/800/400" for i in range(1, 21)
        ]
        categories = list(Categories.objects.all())

        for title, content, img_url in zip(titles, contents, img_urls):
            random_category = random.choice(categories)

            Post.objects.create(
                title=title,
                content=content,
                img_url=img_url,
                categories=random_category 
            )


        self.stdout.write(
            self.style.SUCCESS("20 Posts Created Successfully ✅")
        )

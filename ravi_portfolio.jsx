import { motion } from "framer-motion";
import { Github, Linkedin, Mail, Phone } from "lucide-react";

// Small reusable Section component (moved outside of JSX to avoid build errors)
const Section = ({ id, title, children }) => (
  <section id={id} className="max-w-6xl mx-auto py-20 px-6">
    <h2 className="text-2xl font-bold mb-6 border-b border-gray-200 pb-2">{title}</h2>
    {children}
  </section>
);

export default function Portfolio() {
  return (
    <div className="text-gray-900 bg-white antialiased">
      {/* Header */}
      <header className="fixed top-0 w-full bg-white border-b border-gray-200 z-50">
        <div className="max-w-6xl mx-auto flex justify-between items-center px-6 py-4">
          <h1 className="text-xl font-bold">Ravi Shankar Bedadhala</h1>
          <nav className="space-x-6 text-sm font-medium text-gray-700">
            <a href="#about" className="hover:text-black transition">About</a>
            <a href="#skills" className="hover:text-black transition">Skills</a>
            <a href="#projects" className="hover:text-black transition">Projects</a>
            <a href="#experience" className="hover:text-black transition">Experience</a>
            <a href="#opensource" className="hover:text-black transition">Open Source</a>
            <a href="#contact" className="hover:text-black transition">Contact</a>
          </nav>
        </div>
      </header>

      {/* NOTE: add top padding to avoid fixed header overlap */}
      <main className="pt-20">
        {/* Hero */}
        <section className="min-h-[70vh] flex flex-col justify-center items-center text-center px-4">
          <motion.h1
            className="text-5xl md:text-6xl font-extrabold mb-6"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
          >
            Ravi Shankar Bedadhala
          </motion.h1>
          <p className="text-lg md:text-xl text-gray-600 max-w-2xl">
            Machine Learning Engineer & Software Developer — building AI systems, scalable software, and impactful solutions.
          </p>
          <div className="mt-8 flex flex-col md:flex-row items-center gap-4">
            <div className="flex items-center space-x-2 text-gray-700">
              <Mail className="w-5 h-5" />
              <span>bedadhalaravi5@gmail.com</span>
            </div>
            <div className="flex items-center space-x-2 text-gray-700">
              <Phone className="w-5 h-5" />
              <span>+91 9912914857</span>
            </div>
          </div>
        </section>

        {/* About */}
        <Section id="about" title="About">
          <p className="text-gray-700 leading-relaxed text-lg">
            I’m a B.Tech CS student at Vignan University with a strong foundation in Data Structures, Algorithms, and Machine Learning. Experienced in building chatbots, prediction systems, and contributing to evaluation pipelines in Oritm‑AI.
          </p>
        </Section>

        {/* Skills */}
        <Section id="skills" title="Skills">
          <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-6">
            {["Python", "TensorFlow", "PyTorch", "Scikit-learn", "FastAPI", "Flask", "Django", "AWS", "Docker", "GitHub CI/CD", "Data Mining", "Feature Engineering"].map((skill) => (
              <motion.div
                key={skill}
                whileHover={{ scale: 1.03 }}
                className="border border-gray-200 rounded-lg p-4 text-center text-gray-800 text-sm"
              >
                {skill}
              </motion.div>
            ))}
          </div>
        </Section>

        {/* Projects */}
        <Section id="projects" title="Projects">
          <div className="grid md:grid-cols-2 gap-8">
            {[
              {
                title: "Hybrid Ensemble for Writing Quality Prediction",
                desc: "NLP model leveraging keystroke log data, combining AdaBoost & custom neural nets. Top-100 on Kaggle.",
                link: "https://github.com/ravigithubshankar/Linking-Writing-Quality-Inverted-Ensembiling-Modailites"
              },
              {
                title: "GraphNeurons: Predict AI Model Runtime",
                desc: "Graph-based runtime predictor using ChebNet & GraphSAGE. Achieved 15% higher accuracy.",
                link: "https://github.com/ravigithubshankar/GraphNeurons-Predict-ai-Model-runtime"
              }
            ].map((proj, i) => (
              <motion.div
                key={i}
                whileHover={{ scale: 1.02 }}
                className="border border-gray-200 rounded-lg p-6 hover:shadow transition flex flex-col justify-between"
              >
                <div>
                  <h3 className="text-xl font-semibold mb-2">{proj.title}</h3>
                  <p className="text-gray-600 mb-4 text-sm">{proj.desc}</p>
                </div>
                <a href={proj.link} target="_blank" rel="noopener noreferrer" className="text-indigo-600 text-sm font-medium hover:underline">View on GitHub →</a>
              </motion.div>
            ))}
          </div>
        </Section>

        {/* Experience */}
        <Section id="experience" title="Experience">
          <div className="space-y-10">
            {[
              {
                title: "Machine Learning Engineer Intern — Ignitus",
                period: "Jul 2023 – Oct 2023 (Remote)",
                points: [
                  "Built Python-based Q&A chatbot with Rasa (improved LMS UX).",
                  "Optimized ML/DL models in PyTorch & TensorFlow (20% speedup).",
                  "Collaborated with cross-functional teams to align AI solutions with business needs."
                ]
              },
              {
                title: "Software Engineer Intern — Gagan Apps Pvt. Ltd",
                period: "Apr 2020 – Jun 2020 (Remote)",
                points: [
                  "Built CNN with residual blocks, increased accuracy from 80% to 93%.",
                  "Deployed models via Docker on AWS.",
                  "Improved training efficiency by 75% through algorithmic optimizations."
                ]
              }
            ].map((job, i) => (
              <div key={i} className="border border-gray-200 rounded-lg p-6">
                <h3 className="text-lg font-semibold">{job.title}</h3>
                <p className="text-gray-500 text-sm mb-3">{job.period}</p>
                <ul className="list-disc list-inside text-gray-700 space-y-1 text-sm">
                  {job.points.map((pt, idx) => <li key={idx}>{pt}</li>)}
                </ul>
              </div>
            ))}
          </div>
        </Section>

        {/* Open Source */}
        <Section id="opensource" title="Open Source & Contributions">
          <div className="grid md:grid-cols-2 gap-8">
            <div className="border border-gray-200 rounded-lg p-6">
              <h3 className="text-lg font-semibold mb-2">Open-source Contributions</h3>
              <ul className="list-disc list-inside text-gray-700 space-y-1 text-sm">
                <li><a href="https://github.com/ravigithubshankar/Linking-Writing-Quality-Inverted-Ensembiling-Modailites" target="_blank" rel="noopener noreferrer" className="text-indigo-600 hover:underline">Linking Writing Quality</a></li>
                <li><a href="https://github.com/ravigithubshankar/GraphNeurons-Predict-ai-Model-runtime" target="_blank" rel="noopener noreferrer" className="text-indigo-600 hover:underline">GraphNeurons</a></li>
              </ul>
            </div>
            <div className="border border-gray-200 rounded-lg p-6">
              <h3 className="text-lg font-semibold mb-2">Oritm‑AI Developer</h3>
              <ul className="list-disc list-inside text-gray-700 space-y-1 text-sm">
                <li>Implemented evaluation pipelines for model scoring.</li>
                <li>Integrated cloud deployment with Docker + CI/CD.</li>
                <li>Collaborated on defining metrics & dashboards.</li>
              </ul>
            </div>
          </div>
        </Section>

        {/* Contact */}
        <footer id="contact" className="border-t border-gray-200 py-10 px-6 text-center">
          <p className="mb-2">bedadhalaravi5@gmail.com</p>
          <p className="mb-4">+91 9912914857</p>
          <div className="flex justify-center space-x-6">
            <a href="https://www.linkedin.com/in/ravi-shankar-bedadhala-581750217/" target="_blank" rel="noopener noreferrer"><Linkedin size={22} className="text-gray-700 hover:text-black transition" /></a>
            <a href="https://github.com/ravigithubshankar" target="_blank" rel="noopener noreferrer"><Github size={22} className="text-gray-700 hover:text-black transition" /></a>
          </div>
          <p className="mt-6 text-xs text-gray-500">© {new Date().getFullYear()} Ravi Shankar Bedadhala</p>
        </footer>
      </main>
    </div>
  );
}

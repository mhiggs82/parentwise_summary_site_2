import React, { useState } from 'react';
import Layout from '@theme/Layout';

const glossaryData = [
    {
        letter: 'C', terms: [
            { name: 'Co-regulation', definition: "The process by which one person's nervous system helps regulate another's, essential for infant development and emotional security.", links: '/docs/category/emotional-intelligence' },
            { name: 'Cognitive Load', definition: "The total amount of mental effort being used in the working memory. In parenting, understanding a child's cognitive load helps in giving appropriate instructions.", links: '/docs/category/development' }
        ]
    },
    {
        letter: 'N', terms: [
            { name: 'Neuroplasticity', definition: "The brain's ability to reorganize itself by forming new neural connections throughout life, allowing children to learn and adapt from experiences.", links: '/docs/category/development' }
        ]
    },
    // Add more as needed
];

export default function Glossary() {
    const [search, setSearch] = useState('');

    const filteredGlossary = glossaryData.map(group => ({
        ...group,
        terms: group.terms.filter(t => t.name.toLowerCase().includes(search.toLowerCase()))
    })).filter(group => group.terms.length > 0);

    const letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');

    return (
        <Layout title="Parenting Glossary" description="Demystifying the science of parenting">
            <main className="container" style={{ paddingTop: '80px', paddingBottom: '120px' }}>

                <header style={{ marginBottom: '64px' }}>
                    <h1 style={{ fontSize: '36px', fontWeight: '700', marginBottom: '8px' }}>Parenting Glossary</h1>
                    <p className="text-secondary" style={{ fontSize: '18px' }}>Demystifying the science of parenting, one term at a time.</p>
                </header>

                <div style={{ display: 'flex', gap: '48px' }}>
                    {/* Main Content */}
                    <div style={{ flex: 1 }}>
                        <div style={{ marginBottom: '48px' }}>
                            <input
                                type="text"
                                placeholder="Search terms..."
                                value={search}
                                onChange={(e) => setSearch(e.target.value)}
                                style={{
                                    width: '100%',
                                    background: 'var(--pw-bg-card)',
                                    border: '1px solid var(--pw-border)',
                                    borderRadius: '12px',
                                    padding: '12px 20px',
                                    color: 'white',
                                    fontSize: '16px',
                                    outline: 'none'
                                }}
                            />
                        </div>

                        {/* Letter Nav */}
                        <div style={{
                            display: 'flex',
                            flexWrap: 'wrap',
                            gap: '8px',
                            marginBottom: '48px',
                            position: 'sticky',
                            top: '80px',
                            background: 'var(--pw-bg-canvas)',
                            padding: '12px 0',
                            zIndex: 10
                        }}>
                            {letters.map(l => (
                                <a key={l} href={`#letter-${l}`} style={{
                                    width: '32px',
                                    height: '32px',
                                    display: 'flex',
                                    alignItems: 'center',
                                    justifyContent: 'center',
                                    borderRadius: '8px',
                                    background: glossaryData.some(g => g.letter === l) ? 'rgba(124, 91, 255, 0.1)' : 'transparent',
                                    color: glossaryData.some(g => g.letter === l) ? 'var(--pw-purple)' : 'var(--pw-text-tertiary)',
                                    textDecoration: 'none',
                                    fontWeight: '600',
                                    fontSize: '14px',
                                    border: glossaryData.some(g => g.letter === l) ? '1px solid var(--pw-purple)' : '1px solid transparent'
                                }}>
                                    {l}
                                </a>
                            ))}
                        </div>

                        {filteredGlossary.map(group => (
                            <section key={group.letter} id={`letter-${group.letter}`} style={{ marginBottom: '64px' }}>
                                <h2 style={{
                                    fontSize: '32px',
                                    color: 'var(--pw-purple)',
                                    borderBottom: '2px solid var(--pw-purple)',
                                    paddingBottom: '8px',
                                    marginBottom: '32px'
                                }}>{group.letter}</h2>
                                <div style={{ display: 'flex', flexDirection: 'column', gap: '40px' }}>
                                    {group.terms.map((term, i) => (
                                        <div key={i}>
                                            <h3 style={{ fontSize: '24px', fontWeight: '600', marginBottom: '12px' }}>{term.name}</h3>
                                            <p className="text-secondary" style={{ fontSize: '16px', lineHeight: '1.6', marginBottom: '12px' }}>
                                                {term.definition}
                                            </p>
                                            <a href={term.links} style={{ color: 'var(--pw-purple)', textDecoration: 'none', fontWeight: '500', fontSize: '14px' }}>
                                                Find books on this topic →
                                            </a>
                                        </div>
                                    ))}
                                </div>
                            </section>
                        ))}
                    </div>

                    {/* Sidebar */}
                    <aside style={{ width: '320px', display: 'none' /* Will show on DESKTOP */ }}>
                        <div className="pw-card" style={{ position: 'sticky', top: '100px' }}>
                            <h3 style={{ fontSize: '18px', marginBottom: '16px' }}>Why Terminology Matters</h3>
                            <p className="text-secondary" style={{ fontSize: '14px', lineHeight: '1.5' }}>
                                Understanding these terms empowers parents in conversations with educators, pediatricians, and specialists.
                            </p>
                            <hr style={{ border: 'none', borderBottom: '1px solid var(--pw-border)', margin: '20px 0' }} />
                            <button className="pw-button" style={{ width: '100%', justifyContent: 'center' }}>Suggest a Term</button>
                        </div>
                    </aside>
                </div>

            </main>

            <style jsx>{`
        @media (min-width: 996px) {
          aside { display: block !important; }
        }
      `}</style>
        </Layout>
    );
}

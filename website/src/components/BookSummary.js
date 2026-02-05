import React from 'react';

export default function BookSummary({ data }) {
    if (!data) return null;

    const { meta, hero, why_matters, tabs } = data;

    // Helper to slugify text for IDs
    const slugify = (text) => text.toLowerCase().replace(/[^\w\s-]/g, '').replace(/[\s_]+/g, '-').trim();

    return (
        <div className="book-summary-container" style={{ color: 'var(--pw-text-main)', maxWidth: '900px', margin: '0 auto' }}>
            {/* Hero Section */}
            <section id="summary-overview" style={{
                backgroundColor: 'var(--pw-bg-secondary)',
                borderRadius: '24px',
                padding: '40px',
                marginBottom: '40px',
                border: '1px solid var(--pw-border)',
                boxShadow: '0 10px 30px rgba(0, 0, 0, 0.2)',
                position: 'relative',
                overflow: 'hidden',
                scrollMarginTop: '25vh'
            }}>

                {/* Glow background effect */}
                <div style={{
                    position: 'absolute',
                    top: '-100px',
                    right: '-100px',
                    width: '300px',
                    height: '300px',
                    background: 'radial-gradient(circle, var(--pw-purple-glow) 0%, transparent 70%)',
                    zIndex: 0,
                    pointerEvents: 'none'
                }}></div>

                <div style={{ position: 'relative', zIndex: 1 }}>
                    <div style={{
                        display: 'inline-block',
                        padding: '6px 12px',
                        borderRadius: '12px',
                        backgroundColor: 'rgba(124, 91, 255, 0.15)',
                        border: '1px solid rgba(124, 91, 255, 0.3)',
                        fontSize: '12px',
                        fontWeight: '600',
                        color: 'var(--pw-purple)',
                        textTransform: 'uppercase',
                        letterSpacing: '0.05em',
                        marginBottom: '20px'
                    }}>
                        {hero.badge}
                    </div>

                    <h1 style={{ fontSize: '36px', fontWeight: '800', lineHeight: '1.2', marginBottom: '16px', color: 'var(--pw-text-main)' }}>
                        {meta.title}
                    </h1>
                    <p style={{ fontSize: '18px', color: 'var(--pw-text-secondary)', marginBottom: '12px', maxWidth: '800px' }}>
                        {meta.subtitle}
                    </p>

                    {meta.authors && (
                        <p style={{ fontSize: '16px', color: 'var(--pw-text-tertiary)', marginBottom: '24px', fontWeight: '500' }}>
                            By {meta.authors.join(', ')}
                        </p>
                    )}

                    <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap', marginBottom: '32px' }}>
                        {meta.tags.map((tag, idx) => (
                            <span key={idx} style={{
                                fontSize: '12px',
                                padding: '4px 10px',
                                borderRadius: '8px',
                                backgroundColor: 'var(--pw-bg-tertiary)',
                                color: 'var(--pw-text-secondary)',
                                border: '1px solid var(--pw-border)'
                            }}>
                                {tag}
                            </span>
                        ))}
                    </div>

                    <div style={{
                        display: 'flex',
                        gap: '24px',
                        paddingTop: '24px',
                        borderTop: '1px solid var(--pw-border)'
                    }}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                            <span style={{ fontSize: '20px' }}>💡</span>
                            <div>
                                <div style={{ fontSize: '18px', fontWeight: '700', color: 'var(--pw-purple)' }}>{hero.insights_count}</div>
                                <div style={{ fontSize: '11px', textTransform: 'uppercase', color: 'var(--pw-text-tertiary)' }}>Insights</div>
                            </div>
                        </div>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                            <span style={{ fontSize: '20px' }}>⚡</span>
                            <div>
                                <div style={{ fontSize: '18px', fontWeight: '700', color: 'var(--pw-success)' }}>{hero.actions_count}</div>
                                <div style={{ fontSize: '11px', textTransform: 'uppercase', color: 'var(--pw-text-tertiary)' }}>Actions</div>
                            </div>
                        </div>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                            <span style={{ fontSize: '20px' }}>⏱️</span>
                            <div>
                                <div style={{ fontSize: '18px', fontWeight: '700', color: 'var(--pw-text-main)' }}>{hero.read_time}</div>
                                <div style={{ fontSize: '11px', textTransform: 'uppercase', color: 'var(--pw-text-tertiary)' }}>Read Time</div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            {/* Why It Matters */}
            <section id="why-it-matters" style={{
                marginBottom: '80px',
                padding: '32px',
                backgroundColor: 'rgba(124, 91, 255, 0.05)',
                borderRadius: '20px',
                border: '1px dashed var(--pw-purple-glow)',
                scrollMarginTop: '25vh'
            }}>

                <div style={{ display: 'flex', gap: '20px', alignItems: 'start' }}>
                    <div style={{
                        width: '48px',
                        height: '48px',
                        borderRadius: '12px',
                        backgroundColor: 'var(--pw-purple)',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        fontSize: '24px',
                        flexShrink: 0
                    }}>
                        ❤️
                    </div>
                    <div>
                        <h3 style={{ fontSize: '18px', fontWeight: '700', marginBottom: '8px', color: 'var(--pw-text-main)' }}>Why It Matters</h3>
                        <p style={{ fontSize: '16px', lineHeight: '1.6', color: 'var(--pw-text-secondary)', margin: 0 }}>
                            {why_matters.text}
                        </p>
                    </div>
                </div>
            </section>

            {/* Analysis & Insights Section */}
            <section id="analysis" style={{ marginBottom: '80px', scrollMarginTop: '25vh' }}>

                <div style={{ display: 'flex', alignItems: 'center', gap: '16px', marginBottom: '40px' }}>
                    <h2 style={{ fontSize: '32px', fontWeight: '800', margin: 0 }}>Analysis & Insights</h2>
                    <div style={{ flex: 1, height: '1px', background: 'linear-gradient(to right, var(--pw-border), transparent)' }}></div>
                </div>

                <div style={{ display: 'flex', flexDirection: 'column', gap: '40px' }}>
                    {tabs.analysis.map((item, idx) => (
                        <div key={idx} className="analysis-item" style={{
                            backgroundColor: 'var(--pw-bg-secondary)',
                            borderRadius: '24px',
                            padding: '40px',
                            border: '1px solid var(--pw-border)',
                            boxShadow: '0 4px 20px rgba(0, 0, 0, 0.15)',
                            scrollMarginTop: '25vh'
                        }}>

                            <h2 id={slugify(item.heading)} style={{ fontSize: '24px', fontWeight: '700', marginBottom: '16px', color: 'var(--pw-text-main)' }}>
                                {item.heading}
                            </h2>
                            <p style={{ fontSize: '16px', lineHeight: '1.7', color: 'var(--pw-text-secondary)', marginBottom: '24px' }}>
                                {item.intro_text}
                            </p>

                            {item.insight_card && (
                                <div style={{
                                    padding: '24px',
                                    backgroundColor: 'rgba(0, 229, 160, 0.03)',
                                    borderRadius: '16px',
                                    border: '1px solid rgba(0, 229, 160, 0.1)',
                                    borderLeft: '4px solid var(--pw-insight)',
                                    boxShadow: '0 4px 20px rgba(0, 0, 0, 0.1)',
                                    position: 'relative',
                                    overflow: 'hidden'
                                }}>
                                    <div style={{
                                        position: 'absolute',
                                        top: 0,
                                        right: 0,
                                        width: '60px',
                                        height: '60px',
                                        background: 'radial-gradient(circle at top right, rgba(0, 229, 160, 0.1) 0%, transparent 70%)',
                                        pointerEvents: 'none'
                                    }}></div>

                                    <div style={{ display: 'flex', alignItems: 'center', gap: '12px', marginBottom: '14px' }}>
                                        <div style={{
                                            width: '32px',
                                            height: '32px',
                                            borderRadius: '8px',
                                            backgroundColor: 'rgba(0, 229, 160, 0.1)',
                                            display: 'flex',
                                            alignItems: 'center',
                                            justifyContent: 'center',
                                            fontSize: '18px'
                                        }}>💡</div>
                                        <h4 style={{ margin: 0, fontSize: '16px', fontWeight: '700', color: 'var(--pw-insight)', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
                                            {item.insight_card.title}
                                        </h4>
                                    </div>
                                    <p style={{
                                        margin: 0,
                                        fontSize: '15px',
                                        fontStyle: 'italic',
                                        lineHeight: '1.7',
                                        color: 'var(--pw-text-main)',
                                        paddingLeft: '4px'
                                    }}>
                                        "{item.insight_card.text}"
                                    </p>
                                </div>
                            )}
                        </div>
                    ))}
                </div>
            </section>

            {/* Actionable Framework Section */}
            <section id="actions" style={{ marginBottom: '80px', scrollMarginTop: '25vh' }}>

                <div style={{ display: 'flex', alignItems: 'center', gap: '16px', marginBottom: '40px' }}>
                    <h2 style={{ fontSize: '32px', fontWeight: '800', margin: 0, color: 'var(--pw-success)' }}>Actionable Framework</h2>
                    <div style={{ flex: 1, height: '1px', background: 'linear-gradient(to right, var(--pw-success), transparent)', opacity: 0.3 }}></div>
                </div>

                <div style={{ display: 'flex', flexDirection: 'column', gap: '40px' }}>
                    {tabs.actions.map((item, idx) => (
                        <div key={idx} className="action-process" style={{
                            backgroundColor: 'var(--pw-bg-secondary)',
                            borderRadius: '24px',
                            padding: '40px',
                            border: '1px solid var(--pw-border)',
                            boxShadow: '0 4px 20px rgba(0, 0, 0, 0.15)',
                            scrollMarginTop: '25vh'
                        }}>

                            <h3 id={slugify(item.title)} style={{ fontSize: '20px', fontWeight: '700', marginBottom: '12px', color: 'var(--pw-success)' }}>
                                {item.title}
                            </h3>

                            <p style={{ fontSize: '15px', color: 'var(--pw-text-secondary)', marginBottom: '24px' }}>
                                {item.context}
                            </p>

                            <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
                                {item.steps.map((step, sIdx) => (
                                    <div key={sIdx} style={{ display: 'flex', gap: '16px' }}>
                                        <div style={{
                                            width: '28px',
                                            height: '28px',
                                            borderRadius: '50%',
                                            backgroundColor: 'var(--pw-success-bg)',
                                            border: '1px solid var(--pw-success)',
                                            color: 'var(--pw-success)',
                                            display: 'flex',
                                            alignItems: 'center',
                                            justifyContent: 'center',
                                            fontSize: '12px',
                                            fontWeight: '800',
                                            flexShrink: 0,
                                            marginTop: '2px'
                                        }}>
                                            {sIdx + 1}
                                        </div>
                                        <div>
                                            <span style={{ fontWeight: '700', color: 'var(--pw-text-main)', fontSize: '15px' }}>
                                                {step.bold_title}
                                            </span>
                                            <p style={{ margin: '4px 0 0 0', fontSize: '14px', color: 'var(--pw-text-secondary)', lineHeight: '1.5' }}>
                                                {step.description}
                                            </p>
                                        </div>
                                    </div>
                                ))}
                            </div>
                        </div>
                    ))}
                </div>
            </section>
        </div>
    );
}

import Link from '@docusaurus/Link';

export default function CategoryCard({ name, count, description, to, icon }) {
    return (
        <Link
            to={to}
            className="pw-card-hover"
            style={{
                display: 'flex',
                flexDirection: 'column',
                minHeight: '280px',
                backgroundColor: 'var(--pw-bg-card)',
                border: '1px solid var(--pw-border)',
                borderRadius: '24px',
                padding: '24px',
                boxShadow: '0 4px 12px rgba(0, 0, 0, 0.2)',
                textDecoration: 'none',
                color: 'inherit',
                position: 'relative',
                overflow: 'hidden'
            }}
        >
            {/* Header */}
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '16px' }}>
                <div>
                    <h3 style={{
                        fontSize: '22px',
                        fontWeight: '600',
                        margin: 0,
                        color: 'var(--pw-text-main)'
                    }}>
                        {name}
                    </h3>
                </div>
                <div
                    style={{
                        display: 'inline-flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        height: '40px',
                        width: '40px',
                        borderRadius: '12px',
                        backgroundColor: 'rgba(124, 91, 255, 0.1)',
                        border: '1px solid rgba(124, 91, 255, 0.2)',
                        fontSize: '20px'
                    }}
                >
                    {icon}
                </div>
            </div>

            {/* Description */}
            <div style={{ flex: 1, display: 'flex', flexDirection: 'column', marginTop: '8px' }}>
                <p style={{
                    fontSize: '14px',
                    lineHeight: '1.6',
                    color: 'var(--pw-text-secondary)',
                    margin: 0
                }}>
                    {description}
                </p>
            </div>

            {/* Footer */}
            <div style={{
                marginTop: '20px',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'space-between'
            }}>
                <div>
                    <p style={{
                        fontSize: '11px',
                        color: 'var(--pw-text-tertiary)',
                        margin: '0 0 2px 0'
                    }}>
                        Available guides
                    </p>
                    <p style={{
                        fontSize: '18px',
                        fontWeight: '600',
                        color: 'var(--pw-text-main)',
                        margin: 0
                    }}>
                        {count}
                    </p>
                </div>
                <div style={{
                    display: 'inline-flex',
                    alignItems: 'center',
                    gap: '6px',
                    padding: '8px 16px',
                    borderRadius: '16px',
                    backgroundColor: 'rgba(124, 91, 255, 0.15)',
                    border: '1px solid rgba(124, 91, 255, 0.3)',
                    fontSize: '12px',
                    fontWeight: '500',
                    color: 'var(--pw-purple)'
                }}>
                    Explore
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                        <path d="M5 12h14M12 5l7 7-7 7"/>
                    </svg>
                </div>
            </div>
        </Link>
    );
}

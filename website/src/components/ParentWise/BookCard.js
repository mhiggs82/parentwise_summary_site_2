import Link from '@docusaurus/Link';

export default function BookCard({ badge, title, author, insights, actions, to }) {
    return (
        <Link
            to={to}
            className="pw-card-hover"
            style={{
                flex: '0 0 300px',
                display: 'flex',
                flexDirection: 'column',
                minHeight: '320px',
                backgroundColor: 'var(--pw-bg-card)',
                border: '1px solid var(--pw-border)',
                borderRadius: '20px',
                padding: '20px',
                boxShadow: '0 4px 12px rgba(0, 0, 0, 0.2)',
                textDecoration: 'none',
                color: 'inherit'
            }}
        >
            {/* Header with Badge */}
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '16px' }}>
                <div style={{
                    padding: '4px 10px',
                    borderRadius: '12px',
                    backgroundColor: 'rgba(124, 91, 255, 0.15)',
                    border: '1px solid rgba(124, 91, 255, 0.3)',
                    fontSize: '10px',
                    fontWeight: '600',
                    textTransform: 'uppercase',
                    letterSpacing: '0.05em',
                    color: 'var(--pw-purple)'
                }}>
                    {badge}
                </div>
                <div style={{
                    width: '40px',
                    height: '40px',
                    borderRadius: '12px',
                    backgroundColor: 'rgba(124, 91, 255, 0.1)',
                    border: '1px solid rgba(124, 91, 255, 0.2)',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    fontSize: '20px'
                }}>
                    📖
                </div>
            </div>

            {/* Title and Author */}
            <div style={{ flex: 1 }}>
                <h3 style={{
                    fontSize: '18px',
                    fontWeight: '600',
                    margin: '0 0 8px 0',
                    minHeight: '48px',
                    lineHeight: '1.4',
                    color: 'var(--pw-text-main)'
                }}>
                    {title}
                </h3>
                <p style={{
                    fontSize: '13px',
                    margin: '0 0 16px 0',
                    color: 'var(--pw-text-tertiary)'
                }}>
                    {author}
                </p>
            </div>

            {/* Stats Section */}
            <div style={{
                display: 'flex',
                gap: '12px',
                paddingTop: '16px',
                borderTop: '1px solid var(--pw-border)'
            }}>
                <div style={{
                    flex: 1,
                    padding: '12px',
                    borderRadius: '12px',
                    backgroundColor: 'rgba(124, 91, 255, 0.08)',
                    border: '1px solid rgba(124, 91, 255, 0.15)',
                    textAlign: 'center'
                }}>
                    <p style={{
                        fontSize: '10px',
                        color: 'var(--pw-text-tertiary)',
                        margin: '0 0 4px 0',
                        textTransform: 'uppercase',
                        letterSpacing: '0.05em'
                    }}>
                        Insights
                    </p>
                    <p style={{
                        fontSize: '18px',
                        fontWeight: '600',
                        color: 'var(--pw-purple)',
                        margin: 0
                    }}>
                        {insights}
                    </p>
                </div>
                <div style={{
                    flex: 1,
                    padding: '12px',
                    borderRadius: '12px',
                    backgroundColor: 'rgba(0, 217, 184, 0.08)',
                    border: '1px solid rgba(0, 217, 184, 0.15)',
                    textAlign: 'center'
                }}>
                    <p style={{
                        fontSize: '10px',
                        color: 'var(--pw-text-tertiary)',
                        margin: '0 0 4px 0',
                        textTransform: 'uppercase',
                        letterSpacing: '0.05em'
                    }}>
                        Actions
                    </p>
                    <p style={{
                        fontSize: '18px',
                        fontWeight: '600',
                        color: 'var(--pw-success)',
                        margin: 0
                    }}>
                        {actions}
                    </p>
                </div>
            </div>
        </Link>
    );
}

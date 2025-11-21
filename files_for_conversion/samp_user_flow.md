# SAMP Builder - User Flow & Workflow Design

## The Simple Idea

**Problem**: Organizations have strategic objectives at the board level, but struggle to connect them to operational asset management goals with measurable outcomes and clear accountability.

**Solution**: Define Organizational Objectives → Create SAMP Goals aligned to those objectives → Map to measurable KPIs → Track progress automatically!

---

## Core Concept

### The Strategic Asset Management Planning (SAMP) Hierarchy

SAMP Builder manages **two distinct but connected hierarchies**:

#### Hierarchy 1: Organizational Objectives
```
Organizational Objectives (Board-level strategic priorities)
```
These are standalone strategic priorities defined by leadership to guide the entire organization.

#### Hierarchy 2: SAMP Goal Execution Framework
```
SAMP Goal (Asset management targets)
     ↓
SAMP Objective (Measurable outcomes)
     ↓
SAMP Key Results (KRA - Quantifiable KPIs/metrics)
```

**Strategic Alignment:**
- ✅ Board-level **Organizational Objectives** define "what matters to the enterprise"
- ✅ Asset managers create **SAMP Goals** that support 1-5 organizational objectives (many-to-many)
- ✅ Each goal breaks down into **SAMP Objectives** (specific outcomes)
- ✅ Progress measured via **SAMP Key Results** (KPIs from APS model)

**Database-Driven:**
- ✅ All entities stored in PostgreSQL with proper relationships
- ✅ Many-to-many goal-to-objective linkage via junction table
- ✅ Multi-tenant with `customer_id` isolation
- ✅ Value potential aggregates from goals up to org objectives
- ✅ Automated KPI tracking from Performance Miner integration

**No siloed planning - everything connected from boardroom to field!**

---

## Understanding Key Results vs KPIs

**IMPORTANT**: SAMP Builder creates **Key Results** that are **measured by** KPIs from the Performance Analyser.

### Key Results (What SAMP Builder Creates)
- ✅ **User-defined measurable outcomes** in SAMP Builder
- ✅ Linked to SAMP Objectives
- ✅ **Reference** one or more KPIs for measurement
- ✅ Have baseline, target, and current values
- ✅ Examples: "Reduce emergency repairs by 20%", "Achieve 95% PM compliance"
- ✅ Created and managed in SAMP_Key_Result table

### KPIs / Insights (Pre-configured in Performance Analyser)
- ✅ **Pre-defined performance metrics** in the APS model
- ✅ Configured in Performance Analyser component
- ✅ Stored in `aps_insights_meta` (32+ standard insights)
- ✅ Have calculation logic, benchmarks, and scoring rules
- ✅ Examples: Emergency Repair Ratio, PM Compliance, Field Productivity
- ✅ **SAMP Builder does NOT create KPIs** - it references them

### The Relationship
```
SAMP Key Result: "Reduce emergency repairs by 20%"
    ↓ (measured by)
APS Insight (KPI): "Emergency Repair Ratio"
    ↓ (calculated using)
Performance Analyser: Asset transaction data
```

### How KPI Recommendations Work

When creating a Key Result, the system automatically recommends relevant KPIs based on your strategic choices **AND proven financial impact**:

```
1. SAMP Goal → links to → APS Area (Cost/Throughput/Sustainability/Organizational)
   ↓
2. SAMP Objective → links to → APS Domain (Labor/Work Mgt/Budget/etc.)
   ↓
3. System queries → aps_insights (customer instances) WHERE domain matches
   ↓
4. Joins with → aps_calculation_results (most recent calculations)
   ↓
5. Filters → calculated_financial_value > 0 (only KPIs with proven impact)
   ↓
6. Orders by → calculated_financial_value DESC (highest value first)
   ↓
7. Display top 3-5 KPIs with financial value, score, and current metrics
   ↓
8. User selects KPI(s) to measure Key Result
```

**Example Flow with Financial Filtering**:
- Goal Area: **Cost** (links to Cost area in APS model)
- Objective Domain: **Work Mgt.** (links to Work Management domain)
- System finds: 8 insights in Work Mgt. domain for this customer
- Filters to: 3 insights with `calculated_financial_value > 0`
- **Recommended KPIs** (ordered by financial value):
  1. Emergency Repair Cost - €450,000/year potential value
  2. PM Compliance Rate - €280,000/year potential value
  3. Work Order Backlog - €175,000/year potential value

**Key Differences from Template-Based Recommendations**:
- ✅ Uses **actual calculation results** from `aps_calculation_results` (not just meta templates)
- ✅ Shows only KPIs with **proven financial value** (`calculated_financial_value > 0`)
- ✅ Displays **current calculated values, scores, and financial impact**
- ✅ Orders recommendations by **highest financial value first**
- ✅ Shows **most recent calculation timestamp** for data freshness

This ensures users only see KPIs that are:
1. **Contextually relevant** to their strategic goals (domain match)
2. **Financially impactful** (proven value > 0)
3. **Actionable** (calculated from their actual data)

---

## Complete User Workflow

### Master Flow: From Strategic Objectives to Measurable Goals

```
┌─────────────────────────────────────────────────────────────┐
│ PHASE 1: Strategic Foundation                                │
│ Define Board-Level Organizational Objectives                │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ Step 1: Strategy Team Creates Organizational Objectives     │
│ ───────────────────────────────────────────────────────── │
│ Who: Strategy Director, C-Suite, VP Asset Management       │
│                                                             │
│ Action: Navigate to "Organizational Objectives" section    │
│                                                             │
│ Create New Objective:                                       │
│ ┌─────────────────────────────────────────────────────┐   │
│ │ Option A: Start from Template ⭐                    │   │
│ │                                                      │   │
│ │ Select Template:                                     │   │
│ │ ○ Reduce Total Cost of Ownership by 15%            │   │
│ │ ○ Achieve 95% Equipment Reliability                │   │
│ │ ○ Zero Lost-Time Safety Incidents                  │   │
│ │ ○ Meet Environmental Compliance Targets            │   │
│ │ ○ Improve Workforce Productivity by 20%            │   │
│ │ ... (10+ templates available)                       │   │
│ │                                                      │   │
│ │ [Selected: Reduce TCO by 15%]                       │   │
│ │                                                      │   │
│ │ Option B: Create from Scratch                       │   │
│ └─────────────────────────────────────────────────────┘   │
│                                                             │
│ Customize Objective Metadata:                              │
│ ┌─────────────────────────────────────────────────────┐   │
│ │ Objective Name: [Reduce Total Cost of Ownership    │   │
│ │                  by 15%]                             │   │
│ │                                                      │   │
│ │ Description (Rich Text):                            │   │
│ │ ┌──────────────────────────────────────────────┐   │   │
│ │ │ Achieve 15% reduction in total cost of       │   │   │
│ │ │ ownership across all facilities by 2026      │   │   │
│ │ │ through improved work management, reduced    │   │   │
│ │ │ emergency repairs, and optimized spare       │   │   │
│ │ │ parts inventory.                             │   │   │
│ │ │                                               │   │   │
│ │ │ Strategic Rationale:                         │   │   │
│ │ │ • Current TCO 18% above industry benchmark   │   │   │
│ │ │ • $5M annual savings target                  │   │   │
│ │ └──────────────────────────────────────────────┘   │   │
│ │                                                      │   │
│ │ Owner: [CFO ▼]                                      │   │
│ │ Secondary Owners: [VP Operations, VP Maintenance]   │   │
│ │                                                      │   │
│ │ Category: [Financial ▼]                             │   │
│ │   (Financial, Operational, Safety, Environmental,   │   │
│ │    Growth, Digital, People)                         │   │
│ │                                                      │   │
│ │ Priority: [CRITICAL ▼]                              │   │
│ │   (CRITICAL, HIGH, MEDIUM, LOW)                     │   │
│ │                                                      │   │
│ │ Time Horizon:                                        │   │
│ │   Start: [2024-01-01]  End: [2026-12-31]           │   │
│ │                                                      │   │
│ │ Organizational Scope: [Enterprise-wide ▼]           │   │
│ │                                                      │   │
│ │ Status: [ACTIVE ▼]                                  │   │
│ └─────────────────────────────────────────────────────┘   │
│                                                             │
│ System Actions:                                             │
│ 1. ✓ Generates unique objective_code: ORG-OBJ-2025-001    │
│ 2. ✓ Validates all required fields populated              │
│ 3. ✓ Inserts into Org_Objective table                     │
│ 4. ✓ Links to Org_Objective_Metadata (if from template)   │
│ 5. ✓ Creates audit trail entry                            │
│                                                             │
│ [Save Objective] [Save as Draft]                          │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ Result: Organizational Objectives Library Created           │
│                                                             │
│ Active Organizational Objectives (7):                       │
│ ┌─────────────────────────────────────────────────────┐   │
│ │ 1. Reduce TCO by 15%              [Financial]       │   │
│ │    Priority: CRITICAL  Owner: CFO                   │   │
│ │    Goals: 0  Value: $0  Status: Active ⚠           │   │
│ │                                                      │   │
│ │ 2. Achieve 95% Equipment Reliability [Operational]  │   │
│ │    Priority: CRITICAL  Owner: VP Operations         │   │
│ │    Goals: 0  Value: $0  Status: Active ⚠           │   │
│ │                                                      │   │
│ │ 3. Zero Lost-Time Safety Incidents [Safety]         │   │
│ │    Priority: CRITICAL  Owner: VP Safety             │   │
│ │    Goals: 0  Value: $0  Status: Active ⚠           │   │
│ │                                                      │   │
│ │ ... (4 more objectives)                              │   │
│ └─────────────────────────────────────────────────────┘   │
│                                                             │
│ ⚠ Strategic Gap Alert: All objectives have 0 goals        │
│    Next Step: Create goals that support these objectives   │
└─────────────────────────────────────────────────────────────┘

                          ↓

┌─────────────────────────────────────────────────────────────┐
│ PHASE 2: Goal Definition                                    │
│ Create SAMP Goals Aligned to Organizational Objectives     │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ Step 2: Asset Manager Creates SAMP Goal                     │
│ ───────────────────────────────────────────────────────── │
│ Who: Asset Manager, Plant Manager, Maintenance Manager     │
│                                                             │
│ Context: Starting from APS Performance Analysis insights   │
│ Selected Insights:                                          │
│ • Emergency Repairs (Current: 38%, Gap: 18%, Value: $800K) │
│ • Planning & Scheduling (Current: 65%, Gap: 20%, Value: $450K)│
│                                                             │
│ Action: Click "Create Goal from Insights"                  │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ Step 2A: Define Organizational Scope                        │
│ ───────────────────────────────────────────────────────── │
│                                                             │
│ Multi-Dimensional Scope Selection:                         │
│ ┌─────────────────────────────────────────────────────┐   │
│ │ Country/Region:                                      │   │
│ │ ☑ USA  ☑ Europe  ☐ Middle East  ☐ Asia Pacific     │   │
│ │                                                      │   │
│ │ Site/Facility:                                       │   │
│ │ ☑ Houston Refinery                                  │   │
│ │ ☐ Singapore Terminal                                │   │
│ │ ☐ Rotterdam Plant                                   │   │
│ │                                                      │   │
│ │ Plant/Asset (within Houston Refinery):              │   │
│ │ ☑ Crude Unit                                        │   │
│ │ ☐ Hydrocracker                                      │   │
│ │ ☐ Utilities                                         │   │
│ │                                                      │   │
│ │ Work Center:                                         │   │
│ │ ☑ All Work Centers in Crude Unit                   │   │
│ │                                                      │   │
│ │ Equipment Category: (Optional)                       │   │
│ │ ☐ Rotating Equipment  ☐ Static  ☐ Instrumentation  │   │
│ └─────────────────────────────────────────────────────┘   │
│                                                             │
│ Scope Preview:                                              │
│ ┌─────────────────────────────────────────────────────┐   │
│ │ Selected Scope:                                      │   │
│ │ • Houston Refinery - Crude Unit                     │   │
│ │ • 3 Work Centers                                     │   │
│ │ • 450 Equipment Items                                │   │
│ │ • All equipment categories                          │   │
│ └─────────────────────────────────────────────────────┘   │
│                                                             │
│ [Next: Goal Metadata]                                      │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ Step 2B: Capture Goal Metadata                              │
│ ───────────────────────────────────────────────────────── │
│                                                             │
│ Goal Details:                                               │
│ ┌─────────────────────────────────────────────────────┐   │
│ │ Goal Name (Auto-suggested):                         │   │
│ │ [Emergency Repair Reduction - Houston Crude Unit]   │   │
│ │                                                      │   │
│ │ Description:                                         │   │
│ │ ┌──────────────────────────────────────────────┐   │   │
│ │ │ Reduce emergency repairs in Houston Crude    │   │   │
│ │ │ Unit through improved planning & scheduling  │   │   │
│ │ │ compliance. Focus on proactive maintenance   │   │   │
│ │ │ to prevent equipment failures.               │   │   │
│ │ └──────────────────────────────────────────────┘   │   │
│ │                                                      │   │
│ │ Goal Owner: [John Smith - Crude Unit Manager ▼]    │   │
│ │                                                      │   │
│ │ Stakeholders: (Optional)                            │   │
│ │ [+ Add] Maintenance Planner, Reliability Engineer   │   │
│ │                                                      │   │
│ │ Timeline:                                            │   │
│ │ Start Date: [2025-01-01]                            │   │
│ │ End Date:   [2025-12-31]                            │   │
│ │                                                      │   │
│ │ Priority: [High ▼]                                  │   │
│ │   (Critical, High, Medium, Low)                     │   │
│ │                                                      │   │
│ │ Status: [Active ▼]                                  │   │
│ │   (Draft, Active, On Hold, Completed, Archived)     │   │
│ │                                                      │   │
│ │ Tags: (Optional)                                     │   │
│ │ [Work Management] [Cost Reduction] [+ Add Tag]      │   │
│ └─────────────────────────────────────────────────────┘   │
│                                                             │
│ Linked Insights (Auto-populated from Step 2):              │
│ ┌─────────────────────────────────────────────────────┐   │
│ │ • Emergency Repairs          Value: $800K           │   │
│ │ • Planning & Scheduling      Value: $450K           │   │
│ │                                                      │   │
│ │ Total Value Potential: $1,250,000                   │   │
│ └─────────────────────────────────────────────────────┘   │
│                                                             │
│ System Actions:                                             │
│ 1. ✓ Generates unique goal_code: GOAL-CUST001-EMRG-H7F2-001│
│ 2. ✓ Stores organizational_scope as JSON filter            │
│ 3. ✓ Validates end_date >= start_date                     │
│                                                             │
│ [Next: Strategic Alignment]                                │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ Step 2C: Duplicate Goal Detection ⚠                        │
│ ───────────────────────────────────────────────────────── │
│                                                             │
│ System checks for existing goals with:                     │
│ • Same insights (Emergency Repairs, Planning & Scheduling) │
│ • Overlapping scope (Houston Refinery, Crude Unit)         │
│ • Active or On Hold status                                 │
│                                                             │
│ Duplicate Check Result:                                     │
│ ┌─────────────────────────────────────────────────────┐   │
│ │ ⚠ SIMILAR GOAL FOUND                                │   │
│ │                                                      │   │
│ │ Existing Goal:                                       │   │
│ │ Name: "Reduce Reactive Maintenance - Crude Unit"    │   │
│ │ Owner: Operations Manager                           │   │
│ │ Scope: Houston Refinery - Crude Unit (Rotating Eq.) │   │
│ │ Overlap: 40% (different equipment focus)            │   │
│ │ Status: Active                                       │   │
│ │ Created: 2024-11-01                                  │   │
│ │                                                      │   │
│ │ Actions:                                             │   │
│ │ [View Existing Goal] [Create Anyway] [Cancel]       │   │
│ └─────────────────────────────────────────────────────┘   │
│                                                             │
│ User Reviews: Existing goal focuses on equipment           │
│ reliability. New goal focuses on work planning process.    │
│                                                             │
│ User Action: [Create Anyway]                               │
│                                                             │
│ Justification:                                              │
│ ┌─────────────────────────────────────────────────────┐   │
│ │ [Focuses on work planning process vs. equipment     │   │
│ │  reliability. Different objectives and KPIs.]       │   │
│ └─────────────────────────────────────────────────────┘   │
│                                                             │
│ System logs duplicate warning with justification           │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ Step 2D: Strategic Alignment - Link to Org Objectives ⭐   │
│ ───────────────────────────────────────────────────────── │
│                                                             │
│ System Prompt: "Which organizational objectives does this  │
│ goal support? (Select 1-5)"                                │
│                                                             │
│ Smart Suggestions (Based on goal insights & scope):        │
│ ┌─────────────────────────────────────────────────────┐   │
│ │ Recommended Objectives (High Confidence):            │   │
│ │                                                      │   │
│ │ ☑ Reduce Total Cost of Ownership by 15%            │   │
│ │   Category: Financial  Priority: CRITICAL           │   │
│ │   Owner: CFO                                         │   │
│ │   Current: 4 goals, $3.2M value                     │   │
│ │   Why: Emergency repairs drive TCO                  │   │
│ │                                                      │   │
│ │ ☑ Achieve 95% Equipment Reliability                │   │
│ │   Category: Operational  Priority: CRITICAL         │   │
│ │   Owner: VP Operations                              │   │
│ │   Current: 6 goals, $5.1M value                     │   │
│ │   Why: Reliability reduces emergency work           │   │
│ │                                                      │   │
│ │ Other Available Objectives:                          │   │
│ │                                                      │   │
│ │ ☐ Improve Workforce Productivity by 20%            │   │
│ │   Category: People  Priority: HIGH                  │   │
│ │   Current: 4 goals, $2.8M value                     │   │
│ │                                                      │   │
│ │ ☐ Zero Lost-Time Safety Incidents                  │   │
│ │   Category: Safety  Priority: CRITICAL              │   │
│ │   ... (3 more objectives)                            │   │
│ └─────────────────────────────────────────────────────┘   │
│                                                             │
│ Filter Options:                                             │
│ [✓] Show only compatible categories                        │
│ [ ] Show all objectives                                    │
│                                                             │
│ Search: [Search objectives...]                             │
│                                                             │
│ Selected: 2 of max 5 objectives                            │
│                                                             │
│ Impact Preview:                                             │
│ ┌─────────────────────────────────────────────────────┐   │
│ │ Your goal ($1.25M value) will contribute to:        │   │
│ │                                                      │   │
│ │ 1. Reduce TCO by 15%                                │   │
│ │    Current: 4 goals, $3.2M value                    │   │
│ │    After:   5 goals, $4.45M value (+$1.25M)        │   │
│ │                                                      │   │
│ │ 2. Achieve 95% Equipment Reliability                │   │
│ │    Current: 6 goals, $5.1M value                    │   │
│ │    After:   7 goals, $6.35M value (+$1.25M)        │   │
│ │                                                      │   │
│ │ Note: Full value counted for each objective         │   │
│ └─────────────────────────────────────────────────────┘   │
│                                                             │
│ Validation:                                                 │
│ ✓ Minimum 1 objective selected (Required)                 │
│ ✓ Maximum 5 objectives (Allowed)                          │
│ ⚠ 2 objectives selected (Recommended: 1-3)                │
│                                                             │
│ System Actions:                                             │
│ 1. ✓ Creates linkages in SAMP_Goal_Org_Objective_Mapping  │
│ 2. ✓ Sets contribution_weight = 1.00 (full attribution)   │
│ 3. ✓ Updates value aggregations for both objectives       │
│                                                             │
│ [Next: SAMP Assignment]                                    │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ Step 2E: SAMP Assignment                                    │
│ ───────────────────────────────────────────────────────── │
│                                                             │
│ Assign goal to Strategic Asset Management Plan:            │
│                                                             │
│ Option A: Existing SAMP                                     │
│ ┌─────────────────────────────────────────────────────┐   │
│ │ Available SAMPs (filtered by scope):                │   │
│ │                                                      │   │
│ │ ● 2025 Houston Operations Excellence                │   │
│ │   Period: 2025-01-01 to 2025-12-31                  │   │
│ │   Owner: VP Operations                              │   │
│ │   Goals: 12  Status: Active                         │   │
│ │   Scope: Houston Refinery                           │   │
│ │                                                      │   │
│ │ ○ Q1 2025 Maintenance Improvements                  │   │
│ │   Period: 2025-01-01 to 2025-03-31                  │   │
│ │   Owner: Maintenance Manager                        │   │
│ │   Goals: 5  Status: Active                          │   │
│ │   Scope: Houston Refinery - Maintenance             │   │
│ └─────────────────────────────────────────────────────┘   │
│                                                             │
│ Option B: Create New SAMP                                   │
│ ┌─────────────────────────────────────────────────────┐   │
│ │ [+ Create New SAMP]                                  │   │
│ │                                                      │   │
│ │ If clicked, modal opens:                             │   │
│ │ ┌──────────────────────────────────────────────┐   │   │
│ │ │ SAMP Name: [________________________________]│   │   │
│ │ │ Description: [__________________________]    │   │   │
│ │ │ Start Date: [2025-01-01]                     │   │   │
│ │ │ End Date:   [2025-12-31]                     │   │   │
│ │ │ Owner: [Current User ▼]                      │   │   │
│ │ │ Scope: (Inherited from goal)                │   │   │
│ │ │                                               │   │   │
│ │ │ [Create & Assign]  [Cancel]                  │   │   │
│ │ └──────────────────────────────────────────────┘   │   │
│ └─────────────────────────────────────────────────────┘   │
│                                                             │
│ User Selection: 2025 Houston Operations Excellence         │
│                                                             │
│ System Actions:                                             │
│ 1. ✓ Inserts goal into SAMP_Goal table                    │
│ 2. ✓ Links to SAMP via samp_planner_id FK                 │
│ 3. ✓ Links to APS model via samp_goal_aps_model_mapping_id│
│ 4. ✓ Creates audit trail                                   │
│                                                             │
│ [Next: Review & Confirm]                                   │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ Step 2F: Goal Summary Review & Confirmation                 │
│ ───────────────────────────────────────────────────────── │
│                                                             │
│ Review Goal Before Creation:                                │
│ ┌─────────────────────────────────────────────────────┐   │
│ │ GOAL SUMMARY                                         │   │
│ │ ═══════════════════════════════════════════════════  │   │
│ │                                                      │   │
│ │ Goal Name:                                           │   │
│ │ Emergency Repair Reduction - Houston Crude Unit     │   │
│ │                                                      │   │
│ │ Goal ID: GOAL-CUST001-EMRG-H7F2-001                 │   │
│ │                                                      │   │
│ │ Owner: John Smith (Crude Unit Manager)              │   │
│ │ Timeline: 2025-01-01 to 2025-12-31 (12 months)      │   │
│ │ Priority: High                                       │   │
│ │                                                      │   │
│ │ Organizational Scope:                                │   │
│ │ • Houston Refinery - Crude Unit                     │   │
│ │ • 3 Work Centers, 450 Equipment Items                │   │
│ │                                                      │   │
│ │ Linked Insights (2):                                 │   │
│ │ • Emergency Repairs ($800K)                         │   │
│ │ • Planning & Scheduling ($450K)                     │   │
│ │ Total Value Potential: $1,250,000                   │   │
│ │                                                      │   │
│ │ Strategic Alignment (2 objectives):                 │   │
│ │ • Reduce TCO by 15% (Financial, CRITICAL)           │   │
│ │ • Achieve 95% Reliability (Operational, CRITICAL)   │   │
│ │                                                      │   │
│ │ SAMP Assignment:                                     │   │
│ │ 2025 Houston Operations Excellence                   │   │
│ │                                                      │   │
│ │ [Edit Goal Details] [Edit Alignment] [Edit SAMP]    │   │
│ └─────────────────────────────────────────────────────┘   │
│                                                             │
│ All validations passed ✓                                   │
│                                                             │
│ [Create Goal] [Save as Draft] [Cancel]                    │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ Goal Created Successfully! ✓                                │
│                                                             │
│ ┌─────────────────────────────────────────────────────┐   │
│ │ ✓ Goal "Emergency Repair Reduction - Houston        │   │
│ │   Crude Unit" created successfully                  │   │
│ │                                                      │   │
│ │ Goal ID: GOAL-CUST001-EMRG-H7F2-001                 │   │
│ │ Status: Active                                       │   │
│ │                                                      │   │
│ │ Notifications sent to:                               │   │
│ │ • John Smith (Goal Owner)                           │   │
│ │ • CFO (Org Objective Owner - TCO)                   │   │
│ │ • VP Operations (Org Objective Owner - Reliability) │   │
│ └─────────────────────────────────────────────────────┘   │
│                                                             │
│ What would you like to do next?                            │
│                                                             │
│ ┌─────────────────────────────────────────────────────┐   │
│ │ Recommended Next Steps:                              │   │
│ │                                                      │   │
│ │ [Define Objectives]                                  │   │
│ │  → Create SAMP Objectives under this goal           │   │
│ │                                                      │   │
│ │ [Map KPIs for Tracking]                              │   │
│ │  → Link measurable KPIs to track progress           │   │
│ │                                                      │   │
│ │ [Set Targets]                                        │   │
│ │  → Define target values for KPIs                    │   │
│ │                                                      │   │
│ │ [View Goal Dashboard]                                │   │
│ │  → See goal details and current status              │   │
│ │                                                      │   │
│ │ [Create Another Goal]                                │   │
│ │  → Return to goal creation workflow                 │   │
│ │                                                      │   │
│ │ [Go to SAMP Dashboard]                               │   │
│ │  → View all goals in this SAMP                      │   │
│ └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘

                          ↓

┌─────────────────────────────────────────────────────────────┐
│ PHASE 3: Define Measurable Outcomes                         │
│ Map Goals to KPIs for Progress Tracking                    │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ Step 3: Create SAMP Objectives & Map to Key Results (KPIs) │
│ ───────────────────────────────────────────────────────── │
│ Who: Goal Owner (Asset Manager, Plant Manager)             │
│                                                             │
│ Context: User clicked "Define Objectives" from previous step│
│                                                             │
│ Goal Context Displayed:                                     │
│ ┌─────────────────────────────────────────────────────┐   │
│ │ Current Goal: Emergency Repair Reduction            │   │
│ │ Linked Insights:                                     │   │
│ │ • Emergency Repairs (Gap: 18%, Value: $800K)        │   │
│ │ • Planning & Scheduling (Gap: 20%, Value: $450K)    │   │
│ └─────────────────────────────────────────────────────┘   │
│                                                             │
│ Create Objective #1:                                        │
│ ┌─────────────────────────────────────────────────────┐   │
│ │ Objective Name:                                      │   │
│ │ [Reduce Emergency Work Orders by 40%]               │   │
│ │                                                      │   │
│ │ Description: (Optional)                              │   │
│ │ [Decrease emergency work orders through better      │   │
│ │  predictive maintenance and planning]               │   │
│ │                                                      │   │
│ │ Target Type: [Percentage ▼]                         │   │
│ │ Target Level: [Site ▼]                              │   │
│ │ Target Date: [2025-12-31]                            │   │
│ │                                                      │   │
│ │ Map to APS Domain:                                   │   │
│ │ [Work Management ▼]                                  │   │
│ │   (Auto-linked to SAMP_Objectives_APS_Model_Mapping)│   │
│ └─────────────────────────────────────────────────────┘   │
│                                                             │
│ System inserts into SAMP_Objective table                   │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ Step 3A: Create Key Result & Map to APS Insight (KPI)      │
│ ───────────────────────────────────────────────────────── │
│                                                             │
│ User Action: "Add Key Result"                              │
│                                                             │
│ ┌───────────────────────────────────────────────────────┐ │
│ │ SECTION 1: Key Result Definition                     │ │
│ │                                                        │ │
│ │ Key Result Name: *                                    │ │
│ │ [Reduce Emergency Repair Costs by 40%____________]   │ │
│ │                                                        │ │
│ │ Description:                                          │ │
│ │ [Lower emergency maintenance costs through better___] │ │
│ │ [preventive maintenance compliance_________________] │ │
│ └───────────────────────────────────────────────────────┘ │
│                                                             │
│ ┌───────────────────────────────────────────────────────┐ │
│ │ SECTION 2: Map to APS Insight (KPI Recommendation)   │ │
│ │                                                        │ │
│ │ System automatically recommends KPIs based on:        │ │
│ │ • Goal Area: Cost                                     │ │
│ │ • Objective Domain: Work Mgt.                         │ │
│ │ • Filter Insights (only show KPIs with):               │ │
│ │   calculated_financial_value > 0                      │ │
│ │ • Sort: Highest financial value first                 │ │
│ │                                                        │ │
│ │ Recommended KPIs with Proven Financial Value:         │ │
│ │ (Only showing KPIs with calculated financial impact)  │ │
│ │                                                        │ │
│ │ ☑ Emergency Repair Cost                             │ │
│ │   Code: EMERGENCY_REPAIR_COST                         │ │
│ │   Current Value: 25.5% (reactive ratio)              │ │
│ │   💰 Financial Value: €450,000/year                  │ │
│ │   Score: 62.5/100                                     │ │
│ │   Last Calculated: 2025-11-15 08:30                   │ │
│ │   Description: Ratio between preventive and reactive  │ │
│ │                maintenance cost                       │ │
│ │   Source: aps_calculation_results (insight_id: 23)   │ │
│ │                                                        │ │
│ │ ☐ PM Compliance Rate                                │ │
│ │   Code: PM_COMPLIANCE                                 │ │
│ │   Current Value: 72%                                  │ │
│ │   💰 Financial Value: €280,000/year                  │ │
│ │   Score: 58.0/100                                     │ │
│ │   Last Calculated: 2025-11-15 08:30                   │ │
│ │   Description: Preventive maintenance schedule        │ │
│ │                adherence percentage                   │ │
│ │                                                        │ │
│ │ ☐ Work Order Backlog                                │ │
│ │   Code: WO_BACKLOG                                    │ │
│ │   Current Value: 145 orders                           │ │
│ │   💰 Financial Value: €175,000/year                  │ │
│ │   Score: 54.5/100                                     │ │
│ │   Last Calculated: 2025-11-15 08:30                   │ │
│ │   Description: Number of overdue work orders          │ │
│ │                                                        │ │
│ │ Note: Select 1 or more KPIs to measure this result   │ │
│ │ Only KPIs with calculated financial value > 0 shown  │ │
│ └───────────────────────────────────────────────────────┘ │
│                                                             │
│ System Actions (Background):                               │
│ 1. ✓ Queries aps_insights for customer-specific KPIs      │
│ 2. ✓ Joins with aps_calculation_results (most recent)     │
│ 3. ✓ Filters: domain match AND financial_value > 0        │
│ 4. ✓ Orders by calculated_financial_value DESC            │
│ 5. ✓ Displays top 3-5 KPIs with financial impact          │
│                                                             │
│ Selected: 1 KPI (Emergency Repair Ratio)                   │
│                                                             │
│ [Next: Set Baseline & Targets]                             │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ Step 3B: Capture Baseline Performance                       │
│ ───────────────────────────────────────────────────────── │
│                                                             │
│ System automatically retrieves current values from          │
│ Performance Miner for selected KPIs:                        │
│                                                             │
│ Baseline Capture:                                           │
│ ┌─────────────────────────────────────────────────────┐   │
│ │ KPI 1: Emergency Repair Cost Ratio                  │   │
│ │ ────────────────────────────────────────────────────│   │
│ │ Baseline Value: 38%                                 │   │
│ │ Baseline Date: 2025-01-01 (goal start date)         │   │
│ │ Baseline Period: Last 12 months average             │   │
│ │ Data Source: Performance Miner                      │   │
│ │ Organizational Scope: Houston Crude Unit            │   │
│ │                                                      │   │
│ │ [✓] Use auto-retrieved baseline                     │   │
│ │ [ ] Override manually (with justification)          │   │
│ │                                                      │   │
│ │ ─────────────────────────────────────────────────── │   │
│ │                                                      │   │
│ │ KPI 2: Mean Time To Repair (Emergency)              │   │
│ │ ────────────────────────────────────────────────────│   │
│ │ Baseline Value: 14 hours                            │   │
│ │ Baseline Date: 2025-01-01                           │   │
│ │ Baseline Period: Last 6 months average              │   │
│ │                                                      │   │
│ │ ─────────────────────────────────────────────────── │   │
│ │                                                      │   │
│ │ KPI 3: Emergency Work Order Count                   │   │
│ │ ────────────────────────────────────────────────────│   │
│ │ Baseline Value: 145 per month                       │   │
│ │ Baseline Date: 2025-01-01                           │   │
│ │ Baseline Period: Last 3 months average              │   │
│ └─────────────────────────────────────────────────────┘   │
│                                                             │
│ System Actions:                                             │
│ 1. ✓ Queries Performance Miner API for current values     │
│ 2. ✓ Filters data to goal's organizational scope          │
│ 3. ✓ Stores baselines in SAMP_Key_Result table            │
│ 4. ✓ Links Key Results to SAMP_Objective                  │
│                                                             │
│ [Next: Set Targets]                                        │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ Step 3C: Set Target Values (Epic 5 - Future)               │
│ ───────────────────────────────────────────────────────── │
│                                                             │
│ Define Target Performance for Each KPI:                    │
│ ┌─────────────────────────────────────────────────────┐   │
│ │ KPI 1: Emergency Repair Cost Ratio                  │   │
│ │ ────────────────────────────────────────────────────│   │
│ │ Baseline: 38%                                        │   │
│ │ Target:   [24%]                                      │   │
│ │ Reduction: 14 percentage points (37% improvement)   │   │
│ │                                                      │   │
│ │ Benchmark Reference:                                 │   │
│ │ Industry Best: 20%  Internal Best: 22%              │   │
│ │                                                      │   │
│ │ [✓] Set target = Industry Best (20%)                │   │
│ │ [✓] Set target = Internal Best (22%)                │   │
│ │ [●] Custom target                                    │   │
│ │                                                      │   │
│ │ Target Date: [2025-12-31] (Goal end date)           │   │
│ │                                                      │   │
│ │ ─────────────────────────────────────────────────── │   │
│ │                                                      │   │
│ │ KPI 2: Mean Time To Repair (Emergency)              │   │
│ │ ────────────────────────────────────────────────────│   │
│ │ Baseline: 14 hours                                   │   │
│ │ Target:   [8 hours]                                  │   │
│ │ Reduction: 6 hours (43% improvement)                │   │
│ │                                                      │   │
│ │ ─────────────────────────────────────────────────── │   │
│ │                                                      │   │
│ │ KPI 3: Emergency Work Order Count                   │   │
│ │ ────────────────────────────────────────────────────│   │
│ │ Baseline: 145 per month                              │   │
│ │ Target:   [90 per month]                             │   │
│ │ Reduction: 55 WOs (38% improvement)                 │   │
│ └─────────────────────────────────────────────────────┘   │
│                                                             │
│ System Actions:                                             │
│ 1. ✓ Stores target_value in SAMP_Key_Result table         │
│ 2. ✓ Calculates gap: target - baseline                    │
│ 3. ✓ Enables progress tracking: (current-baseline)/(target-baseline)│
│                                                             │
│ [Save Targets & Activate Tracking]                        │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ Objective & KPIs Configured Successfully! ✓                 │
│                                                             │
│ ┌─────────────────────────────────────────────────────┐   │
│ │ Objective: Reduce Emergency Work Orders by 40%      │   │
│ │                                                      │   │
│ │ Key Results (3 KPIs):                                │   │
│ │ 1. Emergency Repair Cost Ratio                      │   │
│ │    Baseline: 38% → Target: 24%                      │   │
│ │                                                      │   │
│ │ 2. MTTR Emergency                                    │   │
│ │    Baseline: 14 hrs → Target: 8 hrs                 │   │
│ │                                                      │   │
│ │ 3. Emergency WO Count                                │   │
│ │    Baseline: 145/mo → Target: 90/mo                 │   │
│ │                                                      │   │
│ │ ✓ Baseline values captured from Performance Miner   │   │
│ │ ✓ Target values configured                          │   │
│ │ ✓ Automated tracking enabled                        │   │
│ │ ✓ Daily data refresh scheduled                      │   │
│ └─────────────────────────────────────────────────────┘   │
│                                                             │
│ [Add Another Objective] [View Goal Dashboard]             │
└─────────────────────────────────────────────────────────────┘

                          ↓

┌─────────────────────────────────────────────────────────────┐
│ PHASE 4: Monitor Progress                                   │
│ Track Goal Performance Against KPI Targets                 │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ Step 4: Automated KPI Data Refresh (Backend Process)       │
│ ───────────────────────────────────────────────────────── │
│                                                             │
│ Daily Scheduled Job (Runs 3:00 AM):                        │
│                                                             │
│ 1. Performance Miner recalculates all APS metrics (2 AM)   │
│ 2. SAMP Builder scheduled job runs (3 AM):                 │
│    ┌─────────────────────────────────────────────────┐   │
│    │ FOR each active SAMP_Key_Result:                │   │
│    │   • Query Performance Miner API for latest value│   │
│    │   • Filter by organizational scope              │   │
│    │   • Store current_value in SAMP_Key_Result      │   │
│    │   • Update last_refreshed timestamp             │   │
│    │   • Calculate progress %                        │   │
│    │   • Update goal status (On Track/At Risk/Off)   │   │
│    └─────────────────────────────────────────────────┘   │
│                                                             │
│ 3. Detect status changes and trigger notifications         │
│ 4. Check alert thresholds and send alerts if breached      │
│                                                             │
│ Example Update for Goal "Emergency Repair Reduction":      │
│ ┌─────────────────────────────────────────────────────┐   │
│ │ KPI 1: Emergency Repair Cost Ratio                  │   │
│ │ Previous: 38% → Current: 35% (Updated 3:15 AM)     │   │
│ │ Progress: 21% toward target (3 of 14 points)        │   │
│ │                                                      │   │
│ │ KPI 2: MTTR Emergency                                │   │
│ │ Previous: 14 hrs → Current: 13 hrs (Updated 3:15 AM)│   │
│ │ Progress: 17% toward target (1 of 6 hours)          │   │
│ │                                                      │   │
│ │ KPI 3: Emergency WO Count                            │   │
│ │ Previous: 145/mo → Current: 142/mo (Updated 3:15 AM)│   │
│ │ Progress: 5% toward target (3 of 55 WOs)            │   │
│ │                                                      │   │
│ │ Overall Goal Status: AT RISK                        │   │
│ │ (1 KPI on track, 2 KPIs slower than expected)       │   │
│ └─────────────────────────────────────────────────────┘   │
│                                                             │
│ Notifications sent to Goal Owner                           │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ Step 5: Goal Owner Monitors Progress Dashboard              │
│ ───────────────────────────────────────────────────────── │
│ Who: Goal Owner (John Smith - Crude Unit Manager)          │
│                                                             │
│ Action: Opens Goal Dashboard (3 months into goal)          │
│                                                             │
│ Goal Progress Dashboard:                                    │
│ ┌─────────────────────────────────────────────────────┐   │
│ │ GOAL: Emergency Repair Reduction - Houston Crude    │   │
│ │ Status: AT RISK ⚠                                   │   │
│ │ Owner: John Smith  Timeline: 3 of 12 months (25%)   │   │
│ │                                                      │   │
│ │ Strategic Alignment:                                 │   │
│ │ • Reduce TCO by 15% (Financial)                     │   │
│ │ • Achieve 95% Reliability (Operational)             │   │
│ │                                                      │   │
│ │ ══════════════════════════════���════════════════════  │   │
│ │                                                      │   │
│ │ KPI Performance (3 Key Results):                    │   │
│ │                                                      │   │
│ │ 1. Emergency Repair Cost Ratio ✓ ON TRACK          │   │
│ │    ┌────────────────────────────────────────┐      │   │
│ │    │ Baseline    Current        Target       │      │   │
│ │    │   38%         32%            24%        │      │   │
│ │    │    ●──────────●───────────────○         │      │   │
│ │    │             [43% Progress]              │      │   │
│ │    └────────────────────────────────────────┘      │   │
│ │    Trend: ↑ Improving (6 point reduction)          │   │
│ │    Last Updated: 5 hours ago                        │   │
│ │                                                      │   │
│ │    📊 Time Series Chart (3 months):                 │   │
│ │    ┌────────────────────────────────────────┐      │   │
│ │    │ 40%│                                    │      │   │
│ │    │ 38%│●                                   │      │   │
│ │    │ 36%│  ●                                 │      │   │
│ │    │ 34%│    ●                               │      │   │
│ │    │ 32%│      ●────────────────────         │      │   │
│ │    │ 30%│                                    │      │   │
│ │    │ 28%│                                    │      │   │
│ │    │ 26%│                                    │      │   │
│ │    │ 24%│ - - - - - - - Target - - - - - - ○│      │   │
│ │    │    └─────────────────────────────────────│      │   │
│ │    │     Jan   Feb   Mar  ...        Dec     │      │   │
│ │    └────────────────────────────────────────┘      │   │
│ │                                                      │   │
│ │    [Add Comment] [View Details]                     │   │
│ │                                                      │   │
│ │ ─────────────────────────────────────────────────── │   │
│ │                                                      │   │
│ │ 2. MTTR Emergency ⚠ AT RISK                        │   │
│ │    ┌────────────────────────────────────────┐      │   │
│ │    │ Baseline    Current        Target       │      │   │
│ │    │  14 hrs      12 hrs         8 hrs       │      │   │
│ │    │    ●───────────●──────────────○         │      │   │
│ │    │             [33% Progress]              │      │   │
│ │    └────────────────────────────────────────┘      │   │
│ │    Trend: ↑ Improving (slower than expected)       │   │
│ │    Last Updated: 5 hours ago                        │   │
│ │                                                      │   │
│ │    ⚠ Warning: Progress slower than timeline        │   │
│ │       Expected: 50% progress after 25% of timeline │   │
│ │       Actual: 33% progress                          │   │
│ │                                                      │   │
│ │    [Add Comment] [View Details]                     │   │
│ │                                                      │   │
│ │ ─────────────────────────────────────────────────── │   │
│ │                                                      │   │
│ │ 3. Emergency WO Count ❌ OFF TRACK                  │   │
│ │    ┌────────────────────────────────────────┐      │   │
│ │    │ Baseline    Current        Target       │      │   │
│ │    │ 145/mo      138/mo         90/mo        │      │   │
│ │    │    ●─────●──────────────────○           │      │   │
│ │    │             [13% Progress]              │      │   │
│ │    └────────────────────────────────────────┘      │   │
│ │    Trend: → Flat (minimal change)                  │   │
│ │    Last Updated: 5 hours ago                        │   │
│ │                                                      │   │
│ │    ❌ Critical: Far behind expected progress        │   │
│ │       Expected: 50% progress (118 WOs)             │   │
│ │       Actual: 13% progress (138 WOs)               │   │
│ │                                                      │   │
│ │    Recent Comment (2 days ago):                     │   │
│ │    "WO reduction slower than expected. Need to     │   │
│ │     review PM compliance. Meeting with reliability │   │
│ │     engineer scheduled."                            │   │
│ │                                                      │   │
│ │    [Add Comment] [Flag for RCA] [View Details]     │   │
│ └─────────────────────────────────────────────────────┘   │
│                                                             │
│ Overall Goal Health:                                        │
│ ┌─────────────────────────────────────────────────────┐   │
│ │ Progress Summary:                                    │   │
│ │ • 1 of 3 KPIs on track (33%)                        │   │
│ │ • 1 of 3 KPIs at risk (33%)                         │   │
│ │ • 1 of 3 KPIs off track (33%)                       │   │
│ │                                                      │   │
│ │ Automated Status: AT RISK ⚠                         │   │
│ │ (Less than 50% of KPIs on expected trajectory)      │   │
│ │                                                      │   │
│ │ Recommended Actions:                                 │   │
│ │ • Focus on Emergency WO Count improvement           │   │
│ │ • Accelerate MTTR reduction efforts                 │   │
│ │ • Review action plans for off-track KPIs            │   │
│ └─────────────────────────────────────────────────────┘   │
│                                                             │
│ [Add Overall Comment] [Export Dashboard] [Share]          │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ Step 6: Goal Owner Adds Context & Takes Action             │
│ ───────────────────────────────────────────────────────── │
│                                                             │
│ User clicks [Add Comment] on "Emergency WO Count" KPI      │
│                                                             │
│ Comment Entry:                                              │
│ ┌─────────────────────────────────────────────────────┐   │
│ │ Add Context for KPI: Emergency WO Count              │   │
│ │                                                      │   │
│ │ ┌──────────────────────────────────────────────┐   │   │
│ │ │ Investigated WO Count spike in Week 12.      │   │   │
│ │ │ Root cause: Major compressor failure required│   │   │
│ │ │ emergency repair ($250K). Reviewing why PM   │   │   │
│ │ │ didn't catch early warning signs.            │   │   │
│ │ │                                               │   │   │
│ │ │ Action Items:                                │   │   │
│ │ │ 1. Review PM inspection procedures           │   │   │
│ │ │ 2. Implement additional vibration monitoring│   │   │
│ │ │ 3. RCA scheduled for next week               │   │   │
│ │ └──────────────────────────────────────────────┘   │   │
│ │                                                      │   │
│ │ [Attach File] (Optional: Screenshots, reports)      │   │
│ │                                                      │   │
│ │ [Save Comment] [Cancel]                              │   │
│ └─────────────────────────────────────────────────────┘   │
│                                                             │
│ System Actions:                                             │
│ 1. ✓ Stores comment in Entity_Comments table              │
│ 2. ✓ Links to SAMP_Key_Result                             │
│ 3. ✓ Displays comment on KPI chart timeline               │
│ 4. ✓ Notifies stakeholders of update                      │
│                                                             │
│ User also clicks [Flag for RCA]:                           │
│ • Marks KPI for root cause analysis                        │
│ • Assigns RCA task to reliability engineer                 │
│ • Tracks RCA status (Pending → In Progress → Completed)   │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ Step 7: Executive Portfolio Dashboard View                  │
│ ───────────────────────────────────────────────────────── │
│ Who: VP Asset Management, C-Suite                          │
│                                                             │
│ Action: Opens Multi-Goal Portfolio Dashboard               │
│                                                             │
│ Portfolio View - All Active Goals:                         │
│ ┌─────────────────────────────────────────────────────┐   │
│ │ SAMP Portfolio: 2025 Houston Operations Excellence  │   │
│ │ Period: 2025-01-01 to 2025-12-31                    │   │
│ │                                                      │   │
│ │ Summary Metrics:                                     │   │
│ │ • Total Goals: 13                                    │   │
│ │ • Total Value: $18.5M                                │   │
│ │ • On Track: 7 (54%) ✓                               │   │
│ │ • At Risk: 4 (31%) ⚠                                │   │
│ │ • Off Track: 2 (15%) ❌                              │   │
│ │                                                      │   │
│ │ ═══════════════════════════════════════════════════  │   │
│ │                                                      │   │
│ │ Goals List:                                          │   │
│ │                                                      │   │
│ │ Goal Name                    Owner      Status  Prog│   │
│ │ ─────────────────────────────────────────────────── │   │
│ │ Emergency Repair Reduction   J.Smith   ⚠ Risk  43% │   │
│ │ Work Planning Optimization   M.Jones   ✓ Track 68% │   │
│ │ Spare Parts Inventory Mgmt   K.Brown   ✓ Track 72% │   │
│ │ Contractor Cost Optimization T.Wilson  ❌ Off   18% │   │
│ │ Equipment Reliability Improve S.Davis  ✓ Track 55% │   │
│ │ ... (8 more goals)                                   │   │
│ │                                                      │   │
│ │ Filters: [Status ▼] [Owner ▼] [Org Objective ▼]    │   │
│ │ Sort by: [Progress % ▼]                             │   │
│ └─────────────────────────────────────────────────────┘   │
│                                                             │
│ Organizational Objectives Rollup:                          │
│ ┌─────────────────────────────────────────────────────┐   │
│ │ Value by Strategic Objective:                       │   │
│ │                                                      │   │
│ │ 1. Reduce TCO by 15%              $4.45M (5 goals) │   │
│ │    Progress: 58%  Status: ✓ On Track               │   │
│ │                                                      │   │
│ │ 2. Achieve 95% Reliability        $6.35M (7 goals) │   │
│ │    Progress: 52%  Status: ⚠ At Risk                │   │
│ │                                                      │   │
│ │ 3. Zero Safety Incidents          $1.2M (2 goals)  │   │
│ │    Progress: 100% Status: ✓ Completed              │   │
│ │                                                      │   │
│ │ ... (4 more objectives)                              │   │
│ └─────────────────────────────────────────────────────┘   │
│                                                             │
│ [Filter: Off Track Goals] [Export to PowerPoint]          │
│ [View Strategic Alignment Dashboard]                       │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ Step 8: Goal Completion (After 12 months)                  │
│ ───────────────────────────────────────────────────────── │
│                                                             │
│ System Detection (Automated):                               │
│ • All 3 KPIs exceeded targets for 4 consecutive weeks      │
│ • Emergency Repair Cost Ratio: 22% (Target: 24%) ✓        │
│ • MTTR Emergency: 7 hrs (Target: 8 hrs) ✓                 │
│ • Emergency WO Count: 85/mo (Target: 90/mo) ✓             │
│                                                             │
│ Notification Sent to Goal Owner:                           │
│ ┌─────────────────────────────────────────────────────┐   │
│ │ 🎉 Congratulations!                                  │   │
│ │                                                      │   │
│ │ Goal "Emergency Repair Reduction - Houston Crude    │   │
│ │ Unit" has achieved all KPI targets!                 │   │
│ │                                                      │   │
│ │ • All 3 KPIs exceeded targets                       │   │
│ │ • Sustained performance for 4 weeks                 │   │
│ │                                                      │   │
│ │ Would you like to mark this goal as Completed?      │   │
│ │                                                      │   │
│ │ [Review Performance] [Mark as Completed]            │   │
│ └─────────────────────────────────────────────────────┘   │
│                                                             │
│ Goal Owner Reviews Final Dashboard:                        │
│ ┌─────────────────────────────────────────────────────┐   │
│ │ Final Performance Summary:                           │   │
│ │                                                      │   │
│ │ KPI 1: Emergency Repair Cost Ratio                  │   │
│ │   Baseline: 38% → Final: 22% (42% improvement) ✓   │   │
│ │   Target achieved and exceeded                      │   │
│ │                                                      │   │
│ │ KPI 2: MTTR Emergency                                │   │
│ │   Baseline: 14 hrs → Final: 7 hrs (50% improv.) ✓  │   │
│ │   Target achieved and exceeded                      │   │
│ │                                                      │   │
│ │ KPI 3: Emergency WO Count                            │   │
│ │   Baseline: 145/mo → Final: 85/mo (41% improv.) ✓  │   │
│ │   Target achieved and exceeded                      │   │
│ │                                                      │   │
│ │ Total Value Realized: $1,250,000                    │   │
│ │ Timeline: Completed on schedule (12 months)         │   │
│ └─────────────────────────────────────────────────────┘   │
│                                                             │
│ Goal Completion Workflow:                                   │
│ ┌─────────────────────────────────────────────────────┐   │
│ │ Add Final Comments:                                  │   │
│ │ ┌──────────────────────────────────────────────┐   │   │
│ │ │ All sites achieved 95%+ compliance. Incident │   │   │
│ │ │ rate reduced to 1.3, well below target 1.5.  │   │   │
│ │ │ Sustained performance for 4 weeks confirms   │   │   │
│ │ │ goal completion.                             │   │   │
│ │ └──────────────────────────────────────────────┘   │   │
│ │                                                      │   │
│ │ Document Lessons Learned: (Optional)                │   │
│ │ ┌──────────────────────────────────────────────┐   │   │
│ │ │ Key Success Factors:                         │   │   │
│ │ │ • Implemented vibration monitoring early     │   │   │
│ │ │ • Improved PM compliance to 92%              │   │   │
│ │ │ • Cross-training maintenance team            │   │   │
│ │ │                                               │   │   │
│ │ │ Challenges Overcome:                         │   │   │
│ │ │ • Initial compressor failure setback         │   │   │
│ │ │ • Resource constraints in Q2                 │   │   │
│ │ └──────────────────────────────────────────────┘   │   │
│ │                                                      │   │
│ │ [Mark as Completed] [Save as Template]              │   │
│ └─────────────────────────────────────────────────────┘   │
│                                                             │
│ System Actions:                                             │
│ 1. ✓ Updates SAMP_Goal status = 'Completed'               │
│ 2. ✓ Stops KPI data refresh for this goal                 │
│ 3. ✓ Archives goal to "Completed Goals" section           │
│ 4. ✓ Updates org objective progress (removes from active) │
│ 5. ✓ Sends success notification to all stakeholders       │
│ 6. ✓ Saves as success story reference                     │
│                                                             │
│ Goal moved to Completed section - serves as best practice │
│ reference for future similar goals                         │
└─────────────────────────────────────────────────────────────┘
```

---

## Alternative Workflows

### Workflow A: Existing Template Selection (Reuse Goal Configuration)

When creating similar goals across multiple plants:

```
┌─────────────────────────────────────────────────────────────┐
│ Step 2-ALT: Clone Existing Goal                             │
│ ───────────────────────────────────────────────────────── │
│                                                             │
│ User Action: "Create goal similar to existing one"         │
│                                                             │
│ Select Goal to Clone:                                       │
│ ┌─────────────────────────────────────────────────────┐   │
│ │ Available Goals to Clone:                            │   │
│ │                                                      │   │
│ │ ● Emergency Repair Reduction - Houston Crude Unit   │   │
│ │   Created: 2025-01-15                                │   │
│ │   Status: Active                                     │   │
│ │   Objectives: 1  KPIs: 3                            │   │
│ │   Owner: John Smith                                  │   │
│ │                                                      │   │
│ │ ○ Work Planning Optimization - Plant B              │   │
│ │   Created: 2025-02-01                                │   │
│ │   ... (more goals)                                   │   │
│ └─────────────────────────────────────────────────────┘   │
│                                                             │
│ System copies:                                              │
│ • Goal name template                                        │
│ • Description template                                      │
│ • Linked insights                                           │
│ • Organizational objective alignments                       │
│ • Objectives and KPIs structure                            │
│ • Target values (adjustable)                                │
│                                                             │
│ User adjusts:                                               │
│ • Organizational scope (Plant A → Plant B)                 │
│ • Owner (John Smith → Jane Doe)                            │
│ • Start/end dates                                           │
│                                                             │
│ System generates new unique goal_code                       │
│ Checks for duplicates in new scope                          │
│                                                             │
│ Benefit: 5x faster goal creation, consistent approach      │
└─────────────────────────────────────────────────────────────┘
```

### Workflow B: Bulk Goal Creation Across Sites

For regional managers deploying same goal strategy across multiple plants:

```
┌─────────────────────────────────────────────────────────────┐
│ Step 2-BULK: Create Multiple Goals Simultaneously           │
│ ───────────────────────────────────────────────────────── │
│                                                             │
│ User Action: "Bulk Create Goals"                           │
│                                                             │
│ Common Goal Configuration:                                  │
│ ┌─────────────────────────────────────────────────────┐   │
│ │ Goal Name Template: [Cost Optimization - {Plant}]   │   │
│ │ Description: (Common to all)                         │   │
│ │ Insights: Emergency Repairs, Spare Parts Mgmt       │   │
│ │ Timeline: 2025-04-01 to 2025-12-31                  │   │
│ │ Priority: High                                       │   │
│ │ Org Objectives: Reduce TCO                          │   │
│ └─────────────────────────────────────────────────────┘   │
│                                                             │
│ Select Target Scopes (4 plants):                           │
│ ┌─────────────────────────────────────────────────────┐   │
│ │ ☑ Plant A - All Work Centers  Owner: [Manager A ▼] │   │
│ │ ☑ Plant B - All Work Centers  Owner: [Manager B ▼] │   │
│ │ ☑ Plant C - All Work Centers  Owner: [Manager C ▼] │   │
│ │ ☑ Plant D - All Work Centers  Owner: [Manager D ▼] │   │
│ └─────────────────────────────────────────────────────┘   │
│                                                             │
│ System Actions:                                             │
│ 1. ✓ Generates 4 unique goal_codes                        │
│ 2. ✓ Checks each for duplicates in respective scopes      │
│ 3. ✓ Creates 4 SAMP_Goal entries                          │
│ 4. ✓ Creates 4 sets of objective/KPI configurations       │
│ 5. ✓ Sends notifications to all 4 owners                  │
│                                                             │
│ Result:                                                     │
│ 4 goals created in 2 minutes vs. 20 minutes individually   │
│ Consistent configuration across all plants                  │
│ Enables cross-plant performance comparison                  │
└─────────────────────────────────────────────────────────────┘
```

---

## Key Features Summary

### 1. Strategic Alignment Features

| Feature | Description | Schema Tables |
|---------|-------------|---------------|
| **Org Objective Library** | Catalog of board-level strategic objectives | `Org_Objective_Metadata`, `Org_Objective` |
| **Template-Based Creation** | Start from pre-defined objective templates | `Org_Objective_Metadata` |
| **Many-to-Many Goal Linking** | Goals support 1-5 organizational objectives | `SAMP_Goal_Org_Objective_Mapping` |
| **Value Aggregation** | Automatic rollup from goals to objectives | Computed from mappings |
| **Strategic Gap Detection** | Identify objectives with no goals | `vw_Active_Items_By_Customer` |
| **Smart Suggestions** | Auto-suggest objectives based on insights | Application logic |

### 2. Goal Management Features

| Feature | Description | Schema Tables |
|---------|-------------|---------------|
| **Multi-Dimensional Scope** | Define goals by region/site/plant/equipment | **MISSING:** `SAMP_Goal.organizational_scope` (JSON) - P0 |
| **Duplicate Detection** | Prevent overlapping goals in same scope | Application logic + scope hash |
| **Goal Templates** | Reusable goal configurations | Application feature (P1) |
| **Goal Cloning** | Copy successful goals to new scopes | Application feature (P1) |
| **Bulk Creation** | Create multiple similar goals at once | Application feature (P1) |
| **SAMP Assignment** | Organize goals within strategic plans | `SAMP_Planner.planner_id` ↔ `SAMP_Goal.samp_planner_id` |
| **APS Model Mapping** | Link goals to APS framework areas | `SAMP_Goal.samp_goal_aps_model_mapping_id` → `SAMP_Goals_APS_Model_Mapping.area_meta_id` |

### 3. Key Result & KPI Features

| Feature | Description | Schema Tables | Data Flow |
|---------|-------------|---------------|-----------|
| **KPI Recommendation** | Auto-recommend KPIs based on Objective's Domain | `SAMP_Objective` → `SAMP_Objectives_APS_Model_Mapping.domain_meta_id` → `aps_insights_meta` | Domain filtering narrows 32+ KPIs to 3-5 relevant options |
| **Key Result Creation** | Define measurable outcomes for objectives | `SAMP_Key_Result` table | User creates Key Results, not KPIs |
| **KPI Mapping** | Link Key Results to APS Insights (KPIs) with weights | `SAMP_Key_Results_APS_Model_Mapping.insight_meta_id` → `aps_insights_meta.insight_meta_id` | Many-to-many: Key Result ↔ Insights |
| **KPI Metadata Display** | Show KPI name, description, unit, calculation logic | Read `aps_insights_meta.insight_name`, `.description`, `.output_unit`, `.default_calculation_config` | Read-only from Performance Analyser |
| **Baseline Capture** | Store initial performance baseline for Key Results | `SAMP_Key_Result.baseline_value` | Fetched from Performance Miner API |
| **Target Setting** | Define desired performance goals for Key Results | `SAMP_Key_Result.target_value` | User-defined or benchmark-based |
| **Current Value Tracking** | Store latest measured values from Performance Miner | `SAMP_Key_Result.current_value` | Daily refresh from Performance Miner |
| **Automated Data Refresh** | Daily updates from Performance Miner | Scheduled job + API integration | Calls Performance Miner `/api/insights/{id}/current` |
| **Progress Calculation** | Automatic progress % computation | `(current-baseline)/(target-baseline) * 100` | Calculated in application layer |
| **Status Automation** | Auto-update On Track/At Risk/Off Track | Application logic based on progress % | Green: >90%, Yellow: 70-90%, Red: <70% |
| **KPI Alerts** | Threshold breaches and trend warnings | Alert configuration (P1) | Based on current_value vs target_value |
| **Comment Context** | Add explanations for variances | **MISSING:** `Entity_Comments` table - P1 | Links to Key Result entities |

### 4. Dashboard & Reporting

| Feature | Description | Schema Tables |
|---------|-------------|---------------|
| **Goal Dashboard** | Individual goal with all KPI progress | Multiple tables joined |
| **Portfolio Dashboard** | Multi-goal view with status summary | Aggregated from multiple goals |
| **Org Objective Dashboard** | Strategic alignment and value rollup | `vw_SAMP_Hierarchy` |
| **Trend Charts** | Time series visualization of KPIs | Historical KPI data |
| **Benchmark Comparison** | Industry vs. internal best performance | Performance Miner integration |
| **Export Capabilities** | PowerPoint, PDF, Excel exports | Application feature (P1) |

---

## Query Patterns for KPI Recommendations

### Pattern 1: Get Recommended KPIs for Key Result Creation

**Scenario**: User is creating a Key Result under a SAMP Objective

**Data Flow Chain**:
```
SAMP_Objective.samp_objective_id (user's current context)
  ↓
SAMP_Objective.samp_objective_aps_model_mapping_id
  ↓
SAMP_Objectives_APS_Model_Mapping.domain_meta_id
  ↓
aps_insights (customer instances filtered by domain)
  ↓
aps_calculation_results (WHERE calculated_financial_value > 0)
  ↓
Display KPIs with proven financial value, ordered by value
```

**Complete Query**:
```sql
-- Get recommended KPIs based on Objective's Domain AND proven financial value
-- Shows only insights with calculated_financial_value > 0 from most recent calculations
WITH objective_domain AS (
    SELECT domain_meta_id
    FROM SAMP_Objectives_APS_Model_Mapping
    WHERE mapping_id = (
        SELECT samp_objective_aps_model_mapping_id
        FROM SAMP_Objective
        WHERE samp_objective_id = ? -- Current objective ID
    )
),
latest_calculations AS (
    SELECT
        insight_id,
        calculated_financial_value,
        calculated_score,
        currency,
        calculation_outputs,
        calculation_timestamp,
        ROW_NUMBER() OVER (PARTITION BY insight_id ORDER BY calculation_timestamp DESC) as rn
    FROM aps_calculation_results
    WHERE customer_id = ?
      AND calculated_financial_value > 0  -- Only insights with proven financial value
)
SELECT
    i.insight_id,
    i.insight_code,
    i.insight_name,
    i.description,
    i.output_unit,
    i.weight,
    d.domain_name,
    a.area_name,
    lc.calculated_financial_value,
    lc.calculated_score,
    lc.currency,
    lc.calculation_outputs,
    lc.calculation_timestamp as last_calculated_at
FROM aps_insights i
JOIN aps_domains d ON i.domain_id = d.domain_id
JOIN aps_areas a ON d.area_id = a.area_id
JOIN latest_calculations lc ON i.insight_id = lc.insight_id
WHERE i.customer_id = ?
  AND d.domain_meta_id = (SELECT domain_meta_id FROM objective_domain)
  AND lc.rn = 1  -- Most recent calculation only
  AND i.is_active = TRUE
ORDER BY lc.calculated_financial_value DESC;  -- Highest value first
```

**Key Changes from Previous Version**:
- ✅ Uses **aps_insights** (customer instances) instead of aps_insights_meta (templates)
- ✅ Joins with **aps_calculation_results** to get actual calculated values
- ✅ Filters by **calculated_financial_value > 0** (only KPIs with proven financial impact)
- ✅ Orders by **financial value descending** (most impactful KPIs first)
- ✅ Gets **most recent calculation** per insight (ROW_NUMBER window function)
- ✅ Returns **calculation_outputs** JSONB for detailed metrics display

### Pattern 2: Create Key Result with KPI Mapping

**Complete SQL Sequence**:
```sql
-- STEP 1: Create the Key Result
INSERT INTO SAMP_Key_Result (
    key_result_name,
    key_result_desc,
    samp_objective_id,
    baseline_value,
    target_value,
    customer_id,
    status
) VALUES (
    'Reduce emergency repairs by 40%',
    'Lower emergency repair costs through better PM compliance',
    1,  -- Parent objective ID
    25.5,  -- Current baseline from latest calculation: 25.5% reactive ratio
    15.0,  -- Target: 15% (40% reduction goal)
    1,
    'Active'
);

-- Get the newly created key_result_id
SET @key_result_id = LAST_INSERT_ID();

-- STEP 2: Map Key Result to selected APS Insight
-- Note: insight_meta_id links to the template, but user selected this
-- based on aps_insights (customer instance) with calculated_financial_value > 0
INSERT INTO SAMP_Key_Results_APS_Model_Mapping (
    key_result_name,
    insight_meta_id,  -- From aps_insights.insight_meta_id (links to template)
    weight,
    mapping_desc,
    customer_id
) VALUES (
    'Reduce emergency repairs by 40%',
    5,  -- Emergency Repair insight_meta_id (template reference)
    1.0,  -- 100% weight (only one KPI for this Key Result)
    'Primary KPI for measuring emergency repair reduction',
    1
);

-- Get the mapping_id
SET @mapping_id = LAST_INSERT_ID();

-- STEP 3: Store mapping reference in Key Result
UPDATE SAMP_Key_Result
SET samp_key_result_aps_model_mapping_id = @mapping_id
WHERE samp_key_result_id = @key_result_id;
```

**Important Notes**:
- **baseline_value**: Comes from `aps_calculation_results.calculation_outputs` (most recent)
- **insight_meta_id**: SAMP stores the template ID for the link, but recommendations come from `aps_insights` (customer instances) filtered by `calculated_financial_value > 0`
- **Lookup chain**: `SAMP_Key_Results_APS_Model_Mapping.insight_meta_id` → `aps_insights.insight_meta_id` → `aps_insights.insight_id` → `aps_calculation_results.insight_id`

### Pattern 3: Verify Goal→Area→Domain→Insight Chain with Financial Values

**Query to verify the complete hierarchy with calculation results**:
```sql
-- Verify the complete recommendation chain with latest financial values
WITH latest_calc AS (
    SELECT
        insight_id,
        calculated_financial_value,
        calculated_score,
        currency,
        calculation_timestamp,
        ROW_NUMBER() OVER (PARTITION BY insight_id ORDER BY calculation_timestamp DESC) as rn
    FROM aps_calculation_results
    WHERE customer_id = ?
)
SELECT
    sg.goal_name,
    am.area_name,
    so.objective_name,
    dm.domain_name,
    i.insight_name as kpi_name,
    skr.key_result_name,
    skr.baseline_value,
    skr.target_value,
    skr.current_value,
    lc.calculated_financial_value,
    lc.calculated_score,
    lc.currency,
    lc.calculation_timestamp as last_calculated_at
FROM SAMP_Goal sg
JOIN SAMP_Goals_APS_Model_Mapping sgm ON sg.samp_goal_aps_model_mapping_id = sgm.mapping_id
JOIN aps_areas_meta am ON sgm.area_meta_id = am.area_meta_id
JOIN SAMP_Objective so ON so.samp_goal_id = sg.samp_goal_id
JOIN SAMP_Objectives_APS_Model_Mapping som ON so.samp_objective_aps_model_mapping_id = som.mapping_id
JOIN aps_domains_meta dm ON som.domain_meta_id = dm.domain_meta_id
JOIN SAMP_Key_Result skr ON skr.samp_objective_id = so.samp_objective_id
LEFT JOIN SAMP_Key_Results_APS_Model_Mapping skrm ON skr.samp_key_result_aps_model_mapping_id = skrm.mapping_id
LEFT JOIN aps_insights i ON skrm.insight_meta_id = i.insight_meta_id AND i.customer_id = sg.customer_id
LEFT JOIN latest_calc lc ON i.insight_id = lc.insight_id AND lc.rn = 1
WHERE sg.customer_id = ?
ORDER BY sg.goal_name, so.objective_name, skr.key_result_name;
```

**Example Result**:
| goal_name | area_name | objective_name | domain_name | kpi_name | key_result_name | baseline_value | target_value | calculated_financial_value | currency |
|-----------|-----------|----------------|-------------|----------|-----------------|----------------|--------------|---------------------------|----------|
| Reduce Emergency Repair Costs | Cost | Improve Work Order Efficiency | Work Mgt. | Emergency Repair Cost | Reduce emergency repairs by 40% | 25.5 | 15.0 | 450000.00 | EUR |

---

## Database Schema Usage Summary

The SAMP Builder workflow utilizes these tables from [samp_schema.sql](samp_builder/data_model/samp_schema.sql):

### Metadata/Reference Tables

1. **Org_Objective_Metadata** (lines 23-30)
   - Template library for organizational objectives
   - Used in: Step 1 (Objective creation from template)

2. **Org_Objective_APS_Model_Mapping** (lines 33-46)
   - Maps org objectives to APS framework areas (via meta tables)
   - **Schema:** `area_meta_id` → `aps_areas_meta(area_meta_id)`
   - Used in: Strategic alignment layer

3. **SAMP_Goals_APS_Model_Mapping** (lines 49-61)
   - Maps goals to APS performance areas (via meta tables)
   - **Schema:** `area_meta_id` → `aps_areas_meta(area_meta_id)`
   - Used in: Step 2 (Goal creation)

4. **SAMP_Objectives_APS_Model_Mapping** (lines 64-76)
   - Maps objectives to APS domains (via meta tables)
   - **Schema:** `domain_meta_id` → `aps_domains_meta(domain_meta_id)`
   - Used in: Step 3 (Objective creation)

5. **SAMP_Key_Results_APS_Model_Mapping** (lines 79-91)
   - Maps KPIs to APS insights with weights (via meta tables)
   - **Schema:** `insight_meta_id` → `aps_insights_meta(insight_meta_id)`
   - Used in: Step 3A (KPI mapping)

### Transaction Tables

6. **SAMP_Planner** (lines 97-115)
   - Strategic plan configuration
   - **Schema:** `planner_id`, `user_planner_name`, `customer_id`, `owner`, `reporting_stakeholders` (JSON)
   - Used in: Step 2E (SAMP assignment)

7. **Org_Objective** (lines 118-132)
   - Board-level organizational objectives
   - **Schema:** Links to `Org_Objective_APS_Model_Mapping` via `org_objective_APS_model_mapping_id`
   - Used in: Step 1 (Create org objectives)

8. **SAMP_Goal** (lines 135-162)
   - Asset management goals
   - **Schema:**
     - `samp_planner_id` → `SAMP_Planner(planner_id)` FK
     - `samp_goal_aps_model_mapping_id` → `SAMP_Goals_APS_Model_Mapping(mapping_id)` FK
   - **MISSING COLUMN:** `organizational_scope` (JSON) - P0
   - Used in: Step 2 (Goal creation), Step 2D (Strategic linking)

9. **SAMP_Goal_Org_Objective_Mapping** (lines 165-184)
   - Many-to-many goal-to-objective linkage with weights
   - Used in: Step 2D (Strategic alignment)

10. **SAMP_Objective** (lines 187-206)
    - Measurable outcomes under goals
    - **Schema:**
      - `samp_goal_id` → `SAMP_Goal(samp_goal_id)` FK
      - `samp_objective_aps_model_mapping_id` → `SAMP_Objectives_APS_Model_Mapping(mapping_id)` FK
    - Used in: Step 3 (Objective creation)

11. **SAMP_Key_Result** (lines 209-238)
    - Quantifiable KPIs/metrics
    - **Schema:**
      - `samp_objective_id` → `SAMP_Objective(samp_objective_id)` FK
      - `samp_key_result_aps_model_mapping_id` → `SAMP_Key_Results_APS_Model_Mapping(mapping_id)` FK
    - **MISSING COLUMNS:**
      - `baseline_value` DECIMAL - P0
      - `target_value` DECIMAL - P0
      - `current_value` DECIMAL - P0
    - Used in: Step 3A-3C (KPI mapping, baseline, targets), Step 4-5 (Progress tracking)

### Views

12. **vw_SAMP_Hierarchy** (lines 245-261)
    - Complete hierarchy from Org Objective → Key Result
    - Used in: Dashboard views, reporting

13. **vw_Active_Items_By_Customer** (lines 264-271)
    - Customer-level aggregation of active items
    - Used in: Portfolio dashboards, executive summaries

---

## Component Boundaries

### What SAMP Builder DOES:

✅ **Strategic Objective Management**: Define and manage board-level organizational objectives
✅ **Goal Creation**: Create SAMP Goals with multi-dimensional scope (region/site/plant/equipment)
✅ **Strategic Alignment**: Link goals to multiple organizational objectives (many-to-many)
✅ **Objective Definition**: Create measurable SAMP Objectives under goals
✅ **Key Result Creation**: Define Key Results (user-created measurable outcomes)
✅ **Query Calculation Results**: Query `aps_calculation_results` for KPI recommendations with proven financial value
✅ **Financial Value Filtering**: Show only KPIs where `calculated_financial_value > 0`
✅ **KPI Mapping**: Map Key Results to APS Insights (KPIs) via `insight_meta_id` reference
✅ **Display KPI Metrics**: Show calculated values, financial impact, scores, and metadata (read-only)
✅ **Baseline Capture**: Store baseline_value from latest `aps_calculation_results` for Key Results
✅ **Target Setting**: Set target_value for Key Results
✅ **Progress Tracking**: Store and display current_value for Key Results (updated from calculations)
✅ **Status Calculation**: Auto-calculate On Track/At Risk/Off Track status
✅ **Dashboard Visualization**: Display goal/objective/key result hierarchies with progress and financial impact
✅ **Comment Management**: Add context and explanations for variances
✅ **Goal Completion Workflow**: Mark goals as completed with final metrics

### What SAMP Builder DOES NOT DO:

❌ **Create APS Insights (KPIs)**: KPIs are configured in Performance Analyser (`aps_insights` table)
❌ **Modify APS Model Structure**: APS hierarchy (Areas/Domains/Insights) is predefined
❌ **Define KPI Calculation Logic**: Calculation configs stored in `aps_insights.calculation_config` (JSONB)
❌ **Calculate KPI Values**: Performance Analyser calculation engine computes KPI values
❌ **Execute KPI Calculations**: Performance Analyser performs calculations and stores in `aps_calculation_results`
❌ **Store Calculation Results**: `aps_calculation_results` is owned by Performance Analyser
❌ **Manage Benchmarks**: Performance Analyser handles benchmark definition and evaluation
❌ **Manage Work Orders**: Source EAM/CMMS systems manage work order data
❌ **Calculate Raw Metrics**: Performance Miner queries and aggregates transaction data
❌ **Execute Action Plans**: Optimizer component handles project/initiative execution
❌ **Budgeting/Financial Approvals**: External financial systems
❌ **Create Organizational Hierarchy**: Master Data Management systems

### Key Data Flow (V4 Results-Based):

```
Performance Analyser (Owns):
  aps_insights_meta (templates)
    ↓
  aps_insights (customer instances)
    ↓
  aps_calculation_results (time-series calculations)
    - calculated_financial_value
    - calculated_score
    - calculation_outputs (JSONB)
    - calculation_timestamp

SAMP Builder (Reads):
  aps_calculation_results (filtered by calculated_financial_value > 0)
    ↓
  Displays recommendations to user
    ↓
  User creates Key Result
    ↓
  SAMP_Key_Results_APS_Model_Mapping.insight_meta_id
    ↓
  Links back to aps_insights via insight_meta_id
```

---

## Design Principles

### 1. Progressive Disclosure
- Show only relevant information at each step
- Avoid overwhelming users with all options upfront
- Smart suggestions guide decisions

### 2. Reusability & Templates
- Templates for organizational objectives
- Goal cloning for consistency
- Bulk operations for efficiency

### 3. Validation & Early Detection
- Duplicate goal detection before creation
- Strategic alignment enforcement (min 1 objective)
- KPI compatibility checks

### 4. Automation & Integration
- Auto-suggest KPIs based on insights
- Auto-retrieve baselines from Performance Miner
- Auto-calculate progress and status
- Auto-trigger alerts on thresholds

### 5. Visibility & Transparency
- Clear hierarchical structure
- Visual progress indicators
- Time series charts showing trends
- Comment capability for context

### 6. Flexibility
- Support 1-5 organizational objectives per goal
- Optional fields for advanced users
- Multiple KPIs per objective
- Customizable organizational scope

---

## System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    User Interface                        │
│  (Strategy, Goals, Objectives, Key Results, Dashboards) │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              SAMP Builder Component                      │
│  ┌──────────────────────────────────────────────────┐  │
│  │ Org Objective Manager                             │  │
│  │  • Create/update organizational objectives       │  │
│  │  • Template library management                   │  │
│  │  • Strategic alignment tracking                  │  │
│  └──────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────┐  │
│  │ Goal Manager                                      │  │
│  │  • Goal creation and configuration               │  │
│  │  • Multi-dimensional scope definition            │  │
│  │  • Duplicate detection                           │  │
│  │  • Many-to-many org objective linking            │  │
│  │  • APS Area mapping                              │  │
│  └──────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────┐  │
│  │ Objective Manager                                 │  │
│  │  • SAMP Objective creation under Goals           │  │
│  │  • APS Domain mapping                            │  │
│  │  • Value potential tracking                      │  │
│  └──────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────┐  │
│  │ Key Result Manager                                │  │
│  │  • Key Result creation (user-defined outcomes)   │  │
│  │  • Query aps_calculation_results for KPIs        │  │
│  │  • Filter KPIs by financial value > 0            │  │
│  │  • KPI-to-Key Result mapping                     │  │
│  │  • Baseline/target/current value tracking        │  │
│  │  • Progress calculation                          │  │
│  └──────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────┐  │
│  │ Dashboard Generator                               │  │
│  │  • Goal/Objective/Key Result hierarchy views     │  │
│  │  • Financial impact visualization                │  │
│  │  • Portfolio dashboards                          │  │
│  │  • Strategic alignment views                     │  │
│  │  • Executive reporting                           │  │
│  └──────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────┐  │
│  │ Data Refresh Scheduler                            │  │
│  │  • Daily sync from aps_calculation_results       │  │
│  │  • Progress recalculation                        │  │
│  │  • Status updates and alerts                     │  │
│  └──────────────────────────────────────────────────┘  │
└────────────────────┬────────────────────────────────────┘
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
┌──────────────────┐  ┌───────────────────────────────────┐
│   PostgreSQL     │  │  Performance Analyser             │
│   Database       │  │  (Read-only for SAMP)             │
│                  │  │                                   │
│ • SAMP Schema    │  │ • aps_insights (customer KPIs)    │
│ • Metadata Tables│  │ • aps_calculation_results         │
│ • Transaction    │  │   - calculated_financial_value    │
│   Tables         │  │   - calculated_score              │
│                  │  │   - calculation_outputs (JSONB)   │
│                  │  │   - calculation_timestamp         │
└──────────────────┘  └───────────────────────────────────┘
```

---

## Workflow Path Summary

### Path A: Strategic Foundation → Goal Creation (First-Time Setup)

| Step | Action | Duration | Database Operations |
|------|--------|----------|---------------------|
| 1 | Create Organizational Objectives | 10 min | INSERT into Org_Objective |
| 2A-2E | Create SAMP Goal with Alignment | 15 min | INSERT into SAMP_Goal, SAMP_Goal_Org_Objective_Mapping |
| 3 | Define Objectives & Map KPIs | 20 min | INSERT into SAMP_Objective, SAMP_Key_Result |
| 3A-3C | Set Baselines & Targets | 10 min | UPDATE SAMP_Key_Result (baseline, target) |

**Total: ~55 minutes for complete goal setup**

### Path B: Subsequent Goal Creation (Using Templates/Cloning)

| Step | Action | Duration | Database Operations |
|------|--------|----------|---------------------|
| 2-ALT | Clone Existing Goal | 5 min | Copy from existing goal |
| 2A-2E | Adjust Scope & Alignment | 5 min | INSERT with cloned config |

**Total: ~10 minutes using cloning**

### Path C: Ongoing Monitoring (Daily Operations)

| Step | Action | Frequency | Database Operations |
|------|--------|-----------|---------------------|
| 4 | Automated KPI Refresh | Daily (3 AM) | UPDATE SAMP_Key_Result.current_value *(MISSING COLUMN)* |
| 5 | Review Dashboard | Weekly | SELECT from views and tables |
| 6 | Add Comments/Context | As needed | INSERT into Entity_Comments *(MISSING TABLE)* |
| 7 | Portfolio Review | Monthly | SELECT aggregated data |
| 8 | Goal Completion | End of goal | UPDATE SAMP_Goal.status = 'Completed' |

---

**This comprehensive workflow connects strategic planning (boardroom) to operational execution (field) with measurable, data-driven progress tracking!**

---

## ⚠️ Schema Gaps & Required Updates

The following schema updates are **REQUIRED** to fully support this workflow:

### Priority 0 (Critical - Required for MVP)

#### 1. **SAMP_Goal.organizational_scope** (JSON)
```sql
ALTER TABLE SAMP_Goal
ADD COLUMN organizational_scope JSON COMMENT 'Multi-dimensional scope: region/site/plant/equipment';
```
**Impact:** Without this, cannot define goal boundaries or detect duplicates
**Used in:** Step 2A, Step 2C (Duplicate Detection)

#### 2. **SAMP_Key_Result - Baseline/Target/Current Values**
```sql
ALTER TABLE SAMP_Key_Result
ADD COLUMN baseline_value DECIMAL(15,4) COMMENT 'Initial performance baseline',
ADD COLUMN target_value DECIMAL(15,4) COMMENT 'Target performance goal',
ADD COLUMN current_value DECIMAL(15,4) COMMENT 'Latest measured value from Performance Miner';
```
**Impact:** Cannot track progress, calculate % achievement, or auto-update status
**Used in:** Step 3B (Baseline Capture), Step 3C (Target Setting), Step 4 (Data Refresh), Step 5 (Dashboard)

### Priority 1 (Important - Post-MVP)

#### 3. **Entity_Comments Table**
```sql
CREATE TABLE Entity_Comments (
    comment_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    entity_type VARCHAR(50) NOT NULL, -- 'goal', 'objective', 'key_result'
    entity_id INTEGER NOT NULL,
    comment_text TEXT NOT NULL,
    commented_by VARCHAR(255) NOT NULL,
    comment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    customer_id INTEGER NOT NULL,
    INDEX idx_entity (entity_type, entity_id),
    INDEX idx_customer (customer_id)
);
```
**Impact:** No context/explanation capability for variance analysis
**Used in:** Step 6 (Add Comments/Context)

#### 4. **SAMP_Goal - Additional Metadata**
```sql
ALTER TABLE SAMP_Goal
ADD COLUMN goal_code VARCHAR(100) UNIQUE COMMENT 'Unique goal identifier: GOAL-CUST-AREA-HASH-SEQ',
ADD COLUMN owner_id INTEGER COMMENT 'FK to user/employee table',
ADD COLUMN priority VARCHAR(20) DEFAULT 'Medium' COMMENT 'Critical/High/Medium/Low';
```
**Impact:** Missing unique identifiers and ownership tracking
**Used in:** Step 2B (Goal Metadata), Step 2F (Summary Review)

### Integration Requirements

#### 5. **Performance Miner API Integration**
- **Endpoint:** `/api/insights/{insight_id}/baseline`
- **Purpose:** Auto-fetch baseline values for KPIs
- **Frequency:** On-demand during Step 3B

- **Endpoint:** `/api/insights/{insight_id}/current`
- **Purpose:** Daily refresh of current KPI values
- **Frequency:** Daily at 3 AM (scheduled job)

#### 6. **APS Meta Tables (External Dependency)**
The schema now references Performance Analyser v4 meta tables:
- `aps_areas_meta` (4 areas: Cost, Throughput, Sustainability, Organizational)
- `aps_domains_meta` (13 domains: Labor, Contracts, Work Mgt, etc.)
- `aps_insights_meta` (32 insights: Emergency Repair, Field Productivity, etc.)

**Requirement:** Performance Analyser v4 schema must be deployed first

---

## Schema Alignment Status

| Component | Schema Status | Notes |
|-----------|---------------|-------|
| **Org Objectives** | ✅ Complete | All columns present |
| **SAMP Planner** | ✅ Complete | All columns present |
| **SAMP Goals** | ⚠️ Missing Columns | Needs `organizational_scope`, `goal_code`, `owner_id`, `priority` |
| **SAMP Objectives** | ✅ Complete | All core columns present |
| **SAMP Key Results** | ⚠️ Missing Columns | Needs `baseline_value`, `target_value`, `current_value` |
| **APS Model Mapping** | ✅ Updated | Now uses meta table FKs (`area_meta_id`, `domain_meta_id`, `insight_meta_id`) |
| **Junction Tables** | ✅ Complete | `SAMP_Goal_Org_Objective_Mapping` present |
| **Comments/Context** | ❌ Missing Table | `Entity_Comments` not implemented |

**Overall Status:** 70% schema complete - Core hierarchy functional, tracking/metadata gaps exist

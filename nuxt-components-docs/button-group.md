<!-- source: https://ui.nuxt.com/components/button-group --> # ButtonGroup

[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/ButtonGroup.vue)

Group multiple button-like elements together.

## Usage

Wrap multiple [Button](/components/button) within a ButtonGroup to group them
together.

    
    
    <template>
      <UButtonGroup>
        <UButton color="neutral" variant="subtle" label="Button" />
        <UButton color="neutral" variant="outline" icon="i-lucide-chevron-down" />
      </UButtonGroup>
    </template>
    

### Size

Use the `size` prop to change the size of all the buttons.

size

xl

    
    
    <template>
      <UButtonGroup size="xl">
        <UButton color="neutral" variant="subtle" label="Button" />
        <UButton color="neutral" variant="outline" icon="i-lucide-chevron-down" />
      </UButtonGroup>
    </template>
    

### Orientation

Use the `orientation` prop to change the orientation of the buttons. Defaults
to `horizontal`.

orientation

vertical

    
    
    <template>
      <UButtonGroup orientation="vertical">
        <UButton color="neutral" variant="subtle" label="Submit" />
        <UButton color="neutral" variant="outline" label="Cancel" />
      </UButtonGroup>
    </template>
    

## Examples

### With input

You can use components like [Input](/components/input),
[InputMenu](/components/input-menu), [Select](/components/select)
[SelectMenu](/components/select-menu), etc. within a button group.

    
    
    <template>
      <UButtonGroup>
        <UInput color="neutral" variant="outline" placeholder="Enter token" />
    
        <UButton color="neutral" variant="subtle" icon="i-lucide-clipboard" />
      </UButtonGroup>
    </template>
    

### With tooltip

You can use a [Tooltip](/components/tooltip) within a button group.

    
    
    <template>
      <UButtonGroup>
        <UInput color="neutral" variant="outline" placeholder="Enter token" />
    
        <UTooltip text="Copy to clipboard">
          <UButton
            color="neutral"
            variant="subtle"
            icon="i-lucide-clipboard"
          />
        </UTooltip>
      </UButtonGroup>
    </template>
    

### With dropdown

You can use a [DropdownMenu](/components/dropdown-menu) within a button group.

Settings

    
    
    <script setup lang="ts">
    import type { DropdownMenuItem } from '@nuxt/ui'
    
    const items: DropdownMenuItem[] = [
      {
        label: 'Team',
        icon: 'i-lucide-users'
      },
      {
        label: 'Invite users',
        icon: 'i-lucide-user-plus',
        children: [
          {
            label: 'Invite by email',
            icon: 'i-lucide-send-horizontal'
          },
          {
            label: 'Invite by link',
            icon: 'i-lucide-link'
          }
        ]
      },
      {
        label: 'New team',
        icon: 'i-lucide-plus'
      }
    ]
    </script>
    
    <template>
      <UButtonGroup>
        <UButton color="neutral" variant="subtle" label="Settings" />
    
        <UDropdownMenu :items="items">
          <UButton
            color="neutral"
            variant="outline"
            icon="i-lucide-chevron-down"
          />
        </UDropdownMenu>
      </UButtonGroup>
    </template>
    

### With badge

You can use a [Badge](/components/badge) within a button group.

https://

    
    
    <template>
      <UButtonGroup>
        <UBadge color="neutral" variant="outline" size="lg" label="https://" />
    
        <UInput color="neutral" variant="outline" placeholder="www.example.com" />
      </UButtonGroup>
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`size`| `'md'`| ` "md" | "xs" | "sm" | "lg" | "xl"`  
`orientation`| `'horizontal'`| ` "horizontal" | "vertical"`The orientation the buttons are laid out.  
`ui`| | ` {}`  
  
### Slots

Slot |  Type   
---|---  
`default`| `{}`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        buttonGroup: {
          base: 'relative',
          variants: {
            size: {
              xs: '',
              sm: '',
              md: '',
              lg: '',
              xl: ''
            },
            orientation: {
              horizontal: 'inline-flex -space-x-px',
              vertical: 'flex flex-col -space-y-px'
            }
          }
        }
      }
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import ui from '@nuxt/ui/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        ui({
          ui: {
            buttonGroup: {
              base: 'relative',
              variants: {
                size: {
                  xs: '',
                  sm: '',
                  md: '',
                  lg: '',
                  xl: ''
                },
                orientation: {
                  horizontal: 'inline-flex -space-x-px',
                  vertical: 'flex flex-col -space-y-px'
                }
              }
            }
          }
        })
      ]
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import uiPro from '@nuxt/ui-pro/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        uiPro({
          ui: {
            buttonGroup: {
              base: 'relative',
              variants: {
                size: {
                  xs: '',
                  sm: '',
                  md: '',
                  lg: '',
                  xl: ''
                },
                orientation: {
                  horizontal: 'inline-flex -space-x-px',
                  vertical: 'flex flex-col -space-y-px'
                }
              }
            }
          }
        })
      ]
    })
    

Expand code

[ButtonA button element that can act as a link or trigger an
action.](/components/button)[CalendarA calendar component for selecting single
dates, multiple dates or date ranges.](/components/calendar)


<!-- source: https://ui.nuxt.com/components/footer --> # FooterPRO

[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/Footer.vue)

A responsive footer component.

## Usage

The Footer component renders a `<footer>` element.

Use the `left`, `default` and `right` slots to customize the footer.

    
    
    <script setup lang="ts">
    import type { NavigationMenuItem } from '@nuxt/ui'
    
    const items: NavigationMenuItem[] = [
      {
        label: 'Figma Kit',
        to: 'https://www.figma.com/community/file/1288455405058138934',
        target: '_blank'
      },
      {
        label: 'Playground',
        to: 'https://stackblitz.com/edit/nuxt-ui',
        target: '_blank'
      },
      {
        label: 'Roadmap',
        to: '/roadmap'
      },
      {
        label: 'Releases',
        to: 'https://github.com/nuxt/ui/releases',
        target: '_blank'
      }
    ]
    </script>
    
    <template>
      <UFooter>
        <template #left>
          <p class="text-muted text-sm">Copyright © {{ new Date().getFullYear() }}</p>
        </template>
    
        <UNavigationMenu :items="items" variant="link" />
    
        <template #right>
          <UButton
            icon="i-simple-icons-discord"
            color="neutral"
            variant="ghost"
            to="https://chat.nuxt.dev"
            target="_blank"
            aria-label="Discord"
          />
          <UButton
            icon="i-simple-icons-x"
            color="neutral"
            variant="ghost"
            to="https://x.com/nuxt_js"
            target="_blank"
            aria-label="X"
          />
          <UButton
            icon="i-simple-icons-github"
            color="neutral"
            variant="ghost"
            to="https://github.com/nuxt/nuxt"
            target="_blank"
            aria-label="GitHub"
          />
        </template>
      </UFooter>
    </template>
    

In this example, we use the [NavigationMenu](/components/navigation-menu)
component to render the footer links in the center.

## Examples

### Within `app.vue`

Use the Footer component in your `app.vue` or in a layout:

app.vue

    
    
    <script setup lang="ts">
    import type { NavigationMenuItem } from '@nuxt/ui'
    
    const items: NavigationMenuItem[] = [{
      label: 'Figma Kit',
      to: 'https://www.figma.com/community/file/1288455405058138934',
      target: '_blank'
    }, {
      label: 'Playground',
      to: 'https://stackblitz.com/edit/nuxt-ui',
      target: '_blank'
    }, {
      label: 'Roadmap',
      to: '/roadmap'
    }, {
      label: 'Releases',
      to: 'https://github.com/nuxt/ui/releases',
      target: '_blank'
    }]
    </script>
    
    <template>
      <UApp>
        <UHeader />
    
        <UMain>
          <NuxtLayout>
            <NuxtPage />
          </NuxtLayout>
        </UMain>
    
        <USeparator icon="i-simple-icons-nuxtdotjs" type="dashed" class="h-px" />
    
        <UFooter>
          <template #left>
            <p class="text-muted text-sm">
              Copyright © {{ new Date().getFullYear() }}
            </p>
          </template>
    
          <UNavigationMenu :items="items" variant="link" />
    
          <template #right>
            <UButton
              icon="i-simple-icons-discord"
              color="neutral"
              variant="ghost"
              to="https://chat.nuxt.dev"
              target="_blank"
              aria-label="Discord"
            />
            <UButton
              icon="i-simple-icons-x"
              color="neutral"
              variant="ghost"
              to="https://x.com/nuxt_js"
              target="_blank"
              aria-label="X"
            />
            <UButton
              icon="i-simple-icons-github"
              color="neutral"
              variant="ghost"
              to="https://github.com/nuxt/nuxt"
              target="_blank"
              aria-label="GitHub"
            />
          </template>
        </UFooter>
      </UApp>
    </template>
    

In this example, we use the [Separator](/components/separator) component to
add a border above the footer.

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'footer'`| `any`  
`ui`| | ` { root?: ClassNameValue; top?: ClassNameValue; bottom?: ClassNameValue; container?: ClassNameValue; left?: ClassNameValue; center?: ClassNameValue; right?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`left`| `{}`  
`default`| `{}`  
`right`| `{}`  
`top`| `{}`  
`bottom`| `{}`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        footer: {
          slots: {
            root: '',
            top: 'py-8 lg:py-12',
            bottom: 'py-8 lg:py-12',
            container: 'py-8 lg:py-4 lg:flex lg:items-center lg:justify-between lg:gap-x-3',
            left: 'flex items-center justify-center lg:justify-start lg:flex-1 gap-x-1.5 mt-3 lg:mt-0 lg:order-1',
            center: 'mt-3 lg:mt-0 lg:order-2 flex items-center justify-center',
            right: 'lg:flex-1 flex items-center justify-center lg:justify-end gap-x-1.5 lg:order-3'
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
          uiPro: {
            footer: {
              slots: {
                root: '',
                top: 'py-8 lg:py-12',
                bottom: 'py-8 lg:py-12',
                container: 'py-8 lg:py-4 lg:flex lg:items-center lg:justify-between lg:gap-x-3',
                left: 'flex items-center justify-center lg:justify-start lg:flex-1 gap-x-1.5 mt-3 lg:mt-0 lg:order-1',
                center: 'mt-3 lg:mt-0 lg:order-2 flex items-center justify-center',
                right: 'lg:flex-1 flex items-center justify-center lg:justify-end gap-x-1.5 lg:order-3'
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
          uiPro: {
            footer: {
              slots: {
                root: '',
                top: 'py-8 lg:py-12',
                bottom: 'py-8 lg:py-12',
                container: 'py-8 lg:py-4 lg:flex lg:items-center lg:justify-between lg:gap-x-3',
                left: 'flex items-center justify-center lg:justify-start lg:flex-1 gap-x-1.5 mt-3 lg:mt-0 lg:order-1',
                center: 'mt-3 lg:mt-0 lg:order-2 flex items-center justify-center',
                right: 'lg:flex-1 flex items-center justify-center lg:justify-end gap-x-1.5 lg:order-3'
              }
            }
          }
        })
      ]
    })
    

Expand code

[ErrorA pre-built error component with NuxtError
support.](/components/error)[FooterColumnsA list of links as columns to
display in your Footer.](/components/footer-columns)

